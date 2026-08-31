"""Batch upload probability exercise screenshots to MinerU cloud API, extract MD."""
import requests, time, zipfile, io, os, json, glob, sys

TOKEN = 'eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIzNjgwMDY4MSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc4MTI5MzkxMCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTczNDY3NzcxNTAiLCJvcGVuSWQiOm51bGwsInV1aWQiOiIyMjc3ZjM4NS01ZDkyLTRhMTYtODY1NC1lYzAzNjA3MTY3MzciLCJlbWFpbCI6IiIsImV4cCI6MTc4OTA2OTkxMH0.-oOsgQxugdghPbZHG-6wYtVfPyDZSMw5NKiXv-dIJXag0Ofo4TZtKLNHRX4tsXd0K_rS9suaVEwY7bKbE2bP2g'
API = 'https://mineru.net/api/v4'
SRC = r'D:\知识库\课程\概率论\未处理'
OUT = os.path.join(SRC, 'mineru_output')
os.makedirs(OUT, exist_ok=True)

IMAGES_PER_BATCH = 20  # upload up to 20 per batch

images = sorted(glob.glob(os.path.join(SRC, '*.jpg')))
print(f'Found {len(images)} images')

headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
all_results = []

for i in range(0, len(images), IMAGES_PER_BATCH):
    batch = images[i:i+IMAGES_PER_BATCH]
    bi = i // IMAGES_PER_BATCH + 1
    total_batches = (len(images) + IMAGES_PER_BATCH - 1) // IMAGES_PER_BATCH
    print(f'\n=== Batch {bi}/{total_batches}: {len(batch)} images ===')

    # Get upload URLs
    files = [{'name': os.path.basename(f)} for f in batch]
    r = requests.post(f'{API}/file-urls/batch', headers=headers,
        json={'files': files, 'model_version': 'vlm'}, timeout=30)
    if r.status_code != 200:
        print(f'  Error getting URLs: {r.status_code} {r.text[:200]}')
        continue
    data = r.json()['data']
    urls = data['file_urls']
    bid = data['batch_id']

    # Upload all
    for j, (img, url_info) in enumerate(zip(batch, urls)):
        with open(img, 'rb') as f:
            up_resp = requests.put(url_info, data=f, timeout=120)
        print(f'  [{j+1}/{len(batch)}] Upload {os.path.basename(img)}: {up_resp.status_code}')

    # Poll
    print(f'  Polling batch {bid}...')
    for attempt in range(120):
        time.sleep(5)
        r = requests.get(f'{API}/extract-results/batch/{bid}', headers=headers, timeout=30)
        if r.status_code != 200:
            continue
        res = r.json()['data']
        results = res.get('extract_result', [])
        states = [x.get('state', '?') for x in results]
        done_count = sum(1 for s in states if s == 'done')
        failed_count = sum(1 for s in states if s == 'failed')

        if done_count + failed_count == len(results):
            print(f'  All done: {done_count} ok, {failed_count} failed')
            # Download results
            for j, extract in enumerate(results):
                fname = os.path.basename(batch[j])
                if extract.get('state') == 'done':
                    zurl = extract.get('full_zip_url', '')
                    if zurl:
                        r2 = requests.get(zurl, timeout=120)
                        z = zipfile.ZipFile(io.BytesIO(r2.content))
                        out_dir = os.path.join(OUT, fname.replace('.jpg', ''))
                        z.extractall(out_dir)
                        # Find MD
                        for zn in z.namelist():
                            if zn.endswith('.md'):
                                md_content = z.read(zn).decode('utf-8', errors='replace')
                                all_results.append({'file': fname, 'md': md_content})
                                print(f'  [{fname}] MD: {len(md_content)} chars')
                else:
                    print(f'  [{fname}] Failed: {extract.get("err_msg", "")}')
            break
        print(f'  [{attempt+1}] {done_count}/{len(results)} done', end=' ', flush=True)
    else:
        print(f'  Timed out!')

# Save summary
summary_path = os.path.join(OUT, 'all_results.json')
with open(summary_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

# Save merged MD
merged_md = '\n\n---\n\n'.join([f'## {r["file"]}\n\n{r["md"]}' for r in all_results])
merged_path = os.path.join(OUT, 'merged.md')
with open(merged_path, 'w', encoding='utf-8') as f:
    f.write(merged_md)

print(f'\n=== Done! {len(all_results)}/{len(images)} extracted ===')
print(f'Summary: {summary_path}')
print(f'Merged MD: {merged_path}')
