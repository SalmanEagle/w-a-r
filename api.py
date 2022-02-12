import requests
import json
import base64

url = 'https://flowereconomics.com/wp-admin/profile.php'
# url = 'https://flowereconomics.com/wp-json/wp/v2'

user = 'admin'
password = 'A5xz bDWB 9rRP FvxQ 5RpW XWPw'

creds = user + ':' + password

token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {
    'date': '2022-02-06T21:41:00',
    'title': 'First API Post',
    'content': 'This is our first python wordpress api post!',
    'status': 'publish'

}

r = requests.post(url + '/posts', headers=header, json=post)
print(r)
