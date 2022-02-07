import requests
import json
import base64

url = 'https://flowereconomics.com/wp-json/wp/v2'

user = 'salmanshuaib'
password = 'A5xz bDWB 9rRP FvxQ 5RpW XWPw'

creds = user + ':' + password

token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {
    'date': '2019-09-21T10:00:00',
    'title': 'First API Post',
    'content': 'This is our first pythond wordpress api post!',
    'status': 'publish'

}

r = requests.post(url + '/posts', headers=header, json=post)
print(r)
