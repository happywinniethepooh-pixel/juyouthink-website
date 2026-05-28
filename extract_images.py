import zipfile
import os
import shutil

pptx_path = r"C:\Users\12914\WorkBuddy\2026-05-14-task-1\company.pptx"
out_dir = r"C:\Users\12914\WorkBuddy\2026-05-14-task-1\images"
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(pptx_path, 'r') as z:
    # List all image files
    media_files = [f for f in z.namelist() if f.startswith('ppt/media/')]
    print(f"Found {len(media_files)} media files")

    # Extract all images
    for f in media_files:
        filename = os.path.basename(f)
        target = os.path.join(out_dir, filename)
        with z.open(f) as src, open(target, 'wb') as dst:
            shutil.copyfileobj(src, dst)

    # Also list images referenced in slide 4 (client slide)
    slides_rel = [f for f in z.namelist() if 'slides/_rels/slide4.xml.rels' in f]
    for rel in slides_rel:
        with z.open(rel) as f:
            content = f.read().decode('utf-8')
            print(f"\n--- Slide 4 relationships ---")
            print(content[:2000])

print(f"\nImages extracted to: {out_dir}")
