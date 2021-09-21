import xml.etree.ElementTree as ET

# mytree = ET.parse('x1.xml')
# myroot = mytree.getroot()
# print(myroot)

# print(myroot.tag)
# print(myroot.attrib)
# print(myroot[0].tag)

# for x in myroot[0]:
#     print(x.tag, x.attrib)
#
# for x in myroot[0]:
#     print(x.text)

# print(myroot[0].findtext('description'))

# for x in myroot.findall('food'):
#     item = x.find('item').text
#     price = x.find('price').text
#     description = x.find('description').text
#     print(item, price, description)

XML_example_stored_in_a_string = '''<?xml version ="1.0"?>
<States>
    <state name ="TELANGANA">
        <rank>1</rank>
        <neighbor name ="ANDHRA" language ="Telugu"/>
        <neighbor name ="KARNATAKA" language ="Kannada"/>
    </state>
    <state name ="GUJARAT">
        <rank>2</rank>
        <neighbor name ="RAJASTHAN" direction ="N"/>
        <neighbor name ="MADHYA PRADESH" direction ="E"/>
    </state>
    <state name ="KERALA">
        <rank>3</rank>
        <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
    </state>
</States>
'''

root = ET.fromstring(XML_example_stored_in_a_string)
print(root)
# for neighbor in root.iter('neighbor'):
#     print(neighbor.attrib)

for state in root.findall('state'):
    rank = state.find('rank').text
    name = state.get('name')
    print(rank, name)
