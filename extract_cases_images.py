import zipfile
import os
import shutil

pptx_path = r"C:\Users\12914\WorkBuddy\2026-05-14-task-1\cases.pptx"
out_dir = r"C:\Users\12914\WorkBuddy\2026-05-14-task-1\images"

with zipfile.ZipFile(pptx_path, 'r') as z:
    media_files = [f for f in z.namelist() if f.startswith('ppt/media/')]
    print(f"Cases PPT: Found {len(media_files)} media files")

    # Extract all with prefix 'cases_'
    for f in media_files:
        filename = f'cases_{os.path.basename(f)}'
        target = os.path.join(out_dir, filename)
        with z.open(f) as src, open(target, 'wb') as dst:
            shutil.copyfileobj(src, dst)
        print(f'  Extracted: {filename} ({os.path.getsize(target)} bytes)')

# Now let's find which slide has the most images (likely the client logo slide)
print("\n--- Slide relationships summary ---")
for slide_num in range(1, 24):
    rel_path = f'ppt/slides/_rels/slide{slide_num}.xml.rels'
    try:
        with zipfile.ZipFile(pptx_path, 'r') as z:
            content = z.read(rel_path).decode('utf-8')
            img_count = content.count('Target="../media/')
            if img_count > 0:
                print(f'Slide {slide_num}: {img_count} image(s)')
                import re
                targets = re.findall(r'Target="\.\./media/([^"]+)"', content)
                for t in targets:
                    print(f'  -> {t}')
    except:
        pass
