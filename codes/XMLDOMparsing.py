
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("example.xml")
collection = DOMTree.documentElement

persons = collection.getElementsByTagName("pracownik")

for person in persons:
    nodes=person.getElementsByTagName("imie")
    for n in nodes:
        n.firstChild.replaceWholeText("test")

file_handle = open("example2.xml","w")
collection.writexml(writer=file_handle)
file_handle.close()