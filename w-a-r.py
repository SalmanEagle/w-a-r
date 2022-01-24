import requests

CLIENT_ID = 'qonSPuxR3d3sTL7XEOr7IQ'
SECRET_KEY = 'BazBl3t-8GAnOwux_M7fWNb4OMlK9g'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

with open('pw.txt', 'r') as f:
    pw = f.read()

data = {
    'grant_type': 'password',
    'username': 'SalmanEagle',
    'password': pw
}

headers = {'User-Agent': 'w-a-r_API/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
print(res.json())
TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

res = requests.get(
    'https://oauth.reddit.com/r/FlowerEconomics/hot', headers=headers)

res.json()
