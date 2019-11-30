import requests
r = requests.get(url='http://localhost/test/test.php')
print(r.json())
