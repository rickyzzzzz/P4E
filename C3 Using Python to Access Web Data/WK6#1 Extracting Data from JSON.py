import urllib
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
address = urllib.request.urlopen(url)
data = address.read()

total = 0
print('Retrieving: ', url)

while True:
	if len(url)<1: break

	print('Retrieved ', len(data),' characters')

	info = json.loads(data)
	info = info['comments']
	for item in info:
		total += int(item['count'])
	print('Count: ', len(info))
	print('Sum: ', total)
	break