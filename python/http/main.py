import requests
r = requests.get('https://info.cern.ch/hypertext/WWW/TheProject.html')
f = open('request.html', 'w')
f.write(r.text)
print(r.status_code)
print(r.headers)