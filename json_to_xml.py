import json
import xml.etree.ElementTree as ET
import xml.dom.minidom

def json_to_xml(json_data):
    root = ET.Element("root")
    json_to_xml_recursive(json_data, root)
    xml_string = ET.tostring(root, encoding="unicode")
    xml_formatted = xml.dom.minidom.parseString(xml_string)
    return xml_formatted.toprettyxml(indent="  ")

def json_to_xml_recursive(json_data, parent):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            element = ET.SubElement(parent, str(key))
            json_to_xml_recursive(value, element)
    elif isinstance(json_data, list):
        for item in json_data:
            element = ET.SubElement(parent, "item")
            json_to_xml_recursive(item, element)
    else:
        parent.text = str(json_data)

def main():
    with open("input.json", "r") as json_file:
        json_data = json.load(json_file)

    xml_data = json_to_xml(json_data)
    with open("output.xml", "w") as xml_file:
        xml_file.write(xml_data)

if __name__ == "__main__":
    main()
