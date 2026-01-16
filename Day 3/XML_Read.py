import xml.etree.ElementTree as ET
tree=ET.parse("student.xml")
root=tree.getroot()

for student in root.findall("student"):
    id=student.find("id").text
    name = student.find("name").text
    marks = student.find("marks").text
    print(id,name,marks)