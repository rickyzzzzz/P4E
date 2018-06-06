import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
print('Count: ', len(counts))

num = 0
for item in counts:
    cc = item.find('count').text
    num += int(cc)
print('Sum: ', num)