import zipfile
import xml.etree.ElementTree as ET

pptx_path = r"C:\Users\12914\WorkBuddy\2026-05-14-task-1\company.pptx"

def extract_text_from_xml(xml_content):
    root = ET.fromstring(xml_content)
    texts = []
    for elem in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
        if elem.text and elem.text.strip():
            texts.append(elem.text.strip())
    return ' | '.join(texts)

with zipfile.ZipFile(pptx_path, 'r') as z:
    slide_files = sorted([f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')])
    print(f"Total slides: {len(slide_files)}")
    for i, slide_file in enumerate(slide_files, 1):
        with z.open(slide_file) as f:
            content = f.read()
        text = extract_text_from_xml(content)
        if text:
            print(f"\n--- Slide {i} ---")
            print(text[:2000])
