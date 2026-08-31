"""Re-process PDFs via MinerU cloud and save images alongside MD files."""
import requests
import os
import sys
import time
import zipfile
import io
import shutil
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIzNjgwMDY4MSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc4MTI5MzkxMCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTczNDY3NzcxNTAiLCJvcGVuSWQiOm51bGwsInV1aWQiOiIyMjc3ZjM4NS01ZDkyLTRhMTYtODY1NC1lYzAzNjA3MTY3MzciLCJlbWFpbCI6IiIsImV4cCI6MTc4OTA2OTkxMH0.-oOsgQxugdghPbZHG-6wYtVfPyDZSMw5NKiXv-dIJXag0Ofo4TZtKLNHRX4tsXd0K_rS9suaVEwY7bKbE2bP2g"
API = "https://mineru.net/api/v4"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def process_and_save_images(pdf_path, md_dir):
    """Re-process a PDF to extract images alongside MD."""
    pdf_path = Path(pdf_path)
    md_dir = Path(md_dir)
    fname = pdf_path.name

    print(f"\n[PDF] {fname}")

    # Check if images already exist
    existing_md = md_dir / f"{pdf_path.stem}.md"
    if not existing_md.exists():
        print("  [SKIP] MD file not found, skipping")
        return False

    # Check existing image refs in MD
    with open(existing_md, "r", encoding="utf-8") as f:
        content = f.read()
    import re
    img_refs = set(re.findall(r'!\[\]\(images/([^)]+)\)', content))
    print(f"  {len(img_refs)} image references in MD")

    # Check which are missing
    images_dir = md_dir / "images"
    images_dir.mkdir(exist_ok=True)
    missing = [img for img in img_refs if not (images_dir / img).exists()]
    if not missing:
        print(f"  [OK] All {len(img_refs)} images already present")
        return True
    print(f"  {len(missing)}/{len(img_refs)} images missing, re-processing...")

    # Step 1: Get upload URL
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
    print(f"  batch_id={batch_id}")

    # Step 2: Upload
    with open(pdf_path, "rb") as f:
        r = requests.put(upload_url, data=f, timeout=300)
    if r.status_code not in (200, 201, 204):
        print(f"  Upload failed: {r.status_code}")
        return False

    # Step 3: Poll
    saved = 0
    for i in range(180):
        time.sleep(5)
        r = requests.get(f"{API}/extract-results/batch/{batch_id}", headers=HEADERS, timeout=30)
        if r.status_code != 200:
            continue
        res = r.json()["data"]
        extract = res.get("extract_result", [{}])[0]
        state = extract.get("state", "?")

        if state == "done":
            zurl = extract.get("full_zip_url", "")
            if zurl:
                r2 = requests.get(zurl, timeout=120)
                z = zipfile.ZipFile(io.BytesIO(r2.content))
                temp_dir = md_dir / f"_img_temp_{batch_id}"
                z.extractall(temp_dir)

                # Copy images
                for root, dirs, files in os.walk(temp_dir):
                    for fn in files:
                        if fn.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')):
                            src = Path(root) / fn
                            dst = images_dir / fn
                            if fn in missing or not dst.exists():
                                shutil.copy2(src, dst)
                                saved += 1

                shutil.rmtree(temp_dir, ignore_errors=True)
                print(f"  [OK] Saved {saved} new images → {images_dir}")
            break
        elif state == "failed":
            print(f"  [FAIL] {extract.get('err_msg', '')}")
            return False

    return saved > 0 or len(missing) == 0


def main():
    pdf_dir = Path("D:/知识库/课程/大学物理/课件/PDF")
    md_dir = Path("D:/知识库/课程/大学物理/课件/MD")

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    print(f"[INFO] Processing {len(pdfs)} PDFs for image recovery")

    for i, pdf in enumerate(pdfs, 1):
        print(f"\n[{i}/{len(pdfs)}]", end="")
        try:
            process_and_save_images(str(pdf), str(md_dir))
        except Exception as e:
            print(f"  [ERROR] {e}")
        time.sleep(2)  # brief pause between files


if __name__ == "__main__":
    main()
