import xml.etree.ElementTree as ET

mytree = ET.parse('x1.xml')

myroot = mytree.getroot()

# changing attribute of child
for prices in myroot.iter('price'):
    prices.text = str(float(prices.text) + 10)
    prices.set('newprices', 'yes')

# adding new child
# for x in myroot.findall('food'):
#     ET.SubElement(x, 'tasty')
#
# for temp in myroot.iter('tasty'):
#     temp.text = str('YES')

# popping element
# print(myroot[2][0].attrib.pop('name'))

# delete
# print(myroot.remove(myroot[2]))
mytree.write('modified.xml')
