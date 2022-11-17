import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import BD as bd
from lxml import etree as ET




classes = bd.InstrumClass()
root = ET.Element('instruments')
for clas in classes:
    element = ET.SubElement(root, 'class')
    name_inst = ET.SubElement(name_inst, 'name_instrument')
    name_inst.text = clas[0]
    name_class = ET.SubElement(name_class, 'name_class')
    name_class.text = clas[1]


print(f'Content-Type: application/octet-stream; name="artists.xml"\n')
ET.dump(root)

