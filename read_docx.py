import zipfile
import xml.etree.ElementTree as ET

def extract_text(p):
    try:
        with zipfile.ZipFile(p) as d:
            t = ET.fromstring(d.read('word/document.xml'))
            return ' '.join([x.text for x in t.findall('.//w:t', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) if x.text])
    except Exception as e:
        return str(e)

with open('content.txt', 'w', encoding='utf-8') as f:
    f.write('--- Keywords ---\n')
    f.write(extract_text('Fabrication Keyword.docx'))
    f.write('\n\n--- Content ---\n')
    f.write(extract_text('Fabricator Content.docx'))
