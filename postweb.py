import requests

url = 'XXXX/post/'

param ={
    'what':'flag'
}

str = requests.post(url,param)

print(str.text)