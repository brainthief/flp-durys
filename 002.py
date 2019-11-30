import urllib.request
import json
url = 'http://www.fmrc.lt/dcontrol/door.php?id=2'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

#print (cont['status'])

if cont['status'] == "OK" and cont['door'] == "Open": print("Ok")
if cont['status'] == "OK" and cont['door'] == "Deny": print("Soor")

##parcing json
#for item in cont['data']['children']:
#    counter += 1
#    print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
#    print("----")

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
#print("Number of titles: ", counter)
