"""Upload PDF to mineru.net cloud API in batches. vlm model, free 2000 pages/day."""
import argparse, json, os, sys, time, zipfile, io
import requests
import pypdfium2 as pdfium

TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIzNjgwMDY4MSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc4MTI5MzkxMCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTczNDY3NzcxNTAiLCJvcGVuSWQiOm51bGwsInV1aWQiOiIyMjc3ZjM4NS01ZDkyLTRhMTYtODY1NC1lYzAzNjA3MTY3MzciLCJlbWFpbCI6IiIsImV4cCI6MTc4OTA2OTkxMH0.-oOsgQxugdghPbZHG-6wYtVfPyDZSMw5NKiXv-dIJXag0Ofo4TZtKLNHRX4tsXd0K_rS9suaVEwY7bKbE2bP2g"
API = "https://mineru.net/api/v4"
PAGES_PER_BATCH = 150

def main():
    parser = argparse.ArgumentParser(description="MinerU Cloud API PDF to Markdown")
    parser.add_argument("--input", "-i", required=True, help="Input PDF file")
    parser.add_argument("--output", "-o", required=True, help="Output directory")
    args = parser.parse_args()

    pdf_path = os.path.abspath(args.input)
    out_dir = os.path.abspath(args.output)
    os.makedirs(out_dir, exist_ok=True)

    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

    # Get total pages
    pdf = pdfium.PdfDocument(pdf_path)
    total_pages = len(pdf)
    pdf.close()

    batches = []
    for start in range(0, total_pages, PAGES_PER_BATCH):
        end = min(start + PAGES_PER_BATCH - 1, total_pages - 1)
        batches.append((start, end))

    print(f"Total: {total_pages} pages, {len(batches)} batches")
    all_md = []

    for bi, (start, end) in enumerate(batches):
        npages = end - start + 1
        print(f"\n[Batch {bi+1}/{len(batches)}] Pages {start}-{end} ({npages} pages)")

        # Split PDF
        pdf = pdfium.PdfDocument(pdf_path)
        new_pdf = pdfium.PdfDocument.new()
        new_pdf.import_pages(pdf, list(range(start, end + 1)))
        tmp_pdf = os.path.join(out_dir, f"batch_{start}_{end}.pdf")
        new_pdf.save(tmp_pdf)
        new_pdf.close()
        pdf.close()

        # Upload
        r = requests.post(f"{API}/file-urls/batch", headers=headers,
            json={"files": [{"name": f"batch_{start}_{end}.pdf"}], "model_version": "vlm"}, timeout=30)
        if r.status_code != 200:
            print(f"  Error getting URL: {r.status_code} {r.text[:200]}")
            continue
        up = r.json()["data"]["file_urls"][0]
        bid = r.json()["data"]["batch_id"]

        with open(tmp_pdf, "rb") as f:
            r = requests.put(up, data=f, timeout=120)
        print(f"  Uploaded ({r.status_code})")

        # Poll
        done = False
        for _ in range(120):
            time.sleep(5)
            r = requests.get(f"{API}/extract-results/batch/{bid}", headers=headers, timeout=30)
            if r.status_code != 200:
                print(f"  Poll error: {r.status_code}")
                continue
            res = r.json()["data"]
            extract = res.get("extract_result", [{}])[0]
            state = extract.get("state", "?")
            if state == "done":
                zurl = extract.get("full_zip_url", "")
                if zurl:
                    r2 = requests.get(zurl, timeout=120)
                    z = zipfile.ZipFile(io.BytesIO(r2.content))
                    z.extractall(out_dir)
                    print(f"  Done! {len(z.namelist())} files")
                    for n in z.namelist():
                        if n.endswith(".md"):
                            md = z.read(n).decode("utf-8", errors="replace")
                            all_md.append(md)
                            print(f"  MD: {n} ({len(md)} chars)")
                done = True
                break
            elif state == "failed":
                print(f"  Failed: {extract.get('err_msg', '')}")
                done = True
                break
            print(f"  {state}", end=" ", flush=True)

        os.remove(tmp_pdf)
        if not done:
            print(f"  Timeout waiting for batch {bi+1}")

    # Merge all MD
    if all_md:
        merged = "\n\n".join(all_md)
        out_md = os.path.join(out_dir, "merged.md")
        with open(out_md, "w", encoding="utf-8") as f:
            f.write(merged)
        print(f"\n=== Done! Merged: {out_md} ({len(merged)} chars) ===")
        return 0
    else:
        print("No markdown output generated")
        return 1

if __name__ == "__main__":
    sys.exit(main())
