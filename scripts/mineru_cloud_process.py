"""MinerU Cloud API batch processor — process PDFs via mineru.net free API."""
import requests
import os
import sys
import time
import zipfile
import io
import argparse
from pathlib import Path

# Windows GBK fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIzNjgwMDY4MSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc4MTI5MzkxMCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTczNDY3NzcxNTAiLCJvcGVuSWQiOm51bGwsInV1aWQiOiIyMjc3ZjM4NS01ZDkyLTRhMTYtODY1NC1lYzAzNjA3MTY3MzciLCJlbWFpbCI6IiIsImV4cCI6MTc4OTA2OTkxMH0.-oOsgQxugdghPbZHG-6wYtVfPyDZSMw5NKiXv-dIJXag0Ofo4TZtKLNHRX4tsXd0K_rS9suaVEwY7bKbE2bP2g"
API = "https://mineru.net/api/v4"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def process_pdf(pdf_path: str, output_dir: str, subject: str = "") -> bool:
    """Upload a PDF to MinerU cloud and download the markdown result."""
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    fname = pdf_path.name
    stem = pdf_path.stem
    fsize_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"[PDF] {fname} ({fsize_mb:.1f} MB)")
    print(f"[OUT] {output_dir}")

    # Step 1: Get upload URL
    print("[1/4] Getting upload URL...")
    r = requests.post(
        f"{API}/file-urls/batch",
        headers=HEADERS,
        json={"files": [{"name": fname}], "model_version": "vlm"},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"  [FAIL] Status {r.status_code}: {r.text[:200]}")
        return False

    data = r.json()["data"]
    upload_url = data["file_urls"][0]
    batch_id = data["batch_id"]
    print(f"  [OK] batch_id={batch_id}")

    # Step 2: Upload file
    print("[2/4] Uploading file...")
    with open(pdf_path, "rb") as f:
        r = requests.put(upload_url, data=f, timeout=300)
    if r.status_code not in (200, 201, 204):
        print(f"  [FAIL] Upload status {r.status_code}")
        return False
    print(f"  [OK] Uploaded")

    # Step 3: Poll for completion
    print("[3/4] Processing", end="", flush=True)
    md_content = None
    for i in range(180):  # max 15 minutes
        time.sleep(5)
        r = requests.get(f"{API}/extract-results/batch/{batch_id}", headers=HEADERS, timeout=30)
        if r.status_code != 200:
            print(f"\n  [WARN] Poll error: {r.status_code}")
            continue

        res = r.json()["data"]
        extract = res.get("extract_result", [{}])[0]
        state = extract.get("state", "?")

        if state == "done":
            zurl = extract.get("full_zip_url", "")
            if zurl:
                print(" done!")
                r2 = requests.get(zurl, timeout=120)
                z = zipfile.ZipFile(io.BytesIO(r2.content))
                # Extract to temp
                temp_dir = output_dir / f"_temp_{batch_id}"
                z.extractall(temp_dir)
                # Find MD file
                for n in z.namelist():
                    if n.endswith(".md"):
                        md_content = z.read(n).decode("utf-8", errors="replace")
                        print(f"  [MD] {n} ({len(md_content)} chars)")
                        break
                # Cleanup temp
                import shutil
                shutil.rmtree(temp_dir, ignore_errors=True)
            break
        elif state == "failed":
            print(f"\n  [FAIL] {extract.get('err_msg', 'unknown error')}")
            return False
        else:
            print(".", end="", flush=True)

    if md_content is None:
        print("\n  [FAIL] No markdown content in result")
        return False

    # Step 4: Save with frontmatter
    print("[4/4] Saving markdown...")
    frontmatter = f"""---
raw_title: {stem}
subject: {subject or stem}
source: {fname}
status: mineru解析
parser: mineru
---

"""
    out_path = output_dir / f"{stem}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + md_content)

    print(f"  [OK] Saved → {out_path.name} ({len(md_content)} chars)")
    return True


def main():
    parser = argparse.ArgumentParser(description="MinerU Cloud API batch processor")
    parser.add_argument("--input", "-i", required=True, help="PDF file or directory of PDFs")
    parser.add_argument("--output", "-o", required=True, help="Output directory for markdown")
    parser.add_argument("--subject", "-s", default="", help="Course subject name")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)

    # Collect PDFs
    pdfs = []
    if input_path.is_file():
        pdfs = [input_path]
    elif input_path.is_dir():
        pdfs = sorted(input_path.glob("*.pdf")) + sorted(input_path.glob("*.PDF"))

    if not pdfs:
        print(f"[FAIL] No PDFs found in: {input_path}")
        sys.exit(1)

    print(f"[INFO] Found {len(pdfs)} PDF(s) to process")
    success = 0
    fail = 0
    start = time.time()

    for i, pdf in enumerate(pdfs, 1):
        print(f"\n[{i}/{len(pdfs)}]", end="")
        if process_pdf(str(pdf), str(output_dir), args.subject):
            success += 1
        else:
            fail += 1

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"[DONE] Success: {success}, Failed: {fail}, Time: {elapsed:.0f}s")


if __name__ == "__main__":
    main()
