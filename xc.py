from xml.etree.ElementTree import ElementTree,Element

import xml.etree.ElementTree as ET
tree = ET.parse('F:/test/xml/9999936_00000_d_0000001.xml')
root = tree.getroot()
for child in root:
   print(child.tag, child.attrib)
for rank in root.iter('width'):
    new_elem=(int(rank.text)/2+int(rank.text)%2)
    rank.text = str(new_elem)
for rank in root.iter('height'):
    new_elem=(int(rank.text)/2+int(rank.text)%2)
    rank.text = str(new_elem)
for elem in root.iter('xmin'):
    new_elem=(int(elem.text)/2+int(elem.text)%2)
    elem.text = str(new_elem)
for elem in root.iter('ymin'):
    new_elem=(int(elem.text)/2+int(elem.text)%2)
    elem.text = str(new_elem)
for elem in root.iter('xmax'):
    new_elem=(int(elem.text)/2+int(elem.text)%2)
    elem.text = str(new_elem)
for elem in root.iter('ymax'):
    new_elem=(int(elem.text)/2+int(elem.text)%2)
    elem.text = str(new_elem)
tree.write('F:/test/changexml/1.xml')