
# This program calls pastepin api, with generates api_user_key
# Then this program prints new api_user_key
import requests
import configparser

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_name = config['KEYS']['api_user_name']
api_user_password = config['KEYS']['api_user_password']

url = 'https://pastebin.com/api/api_login.php'

body = {'api_dev_key':api_dev_key,
        'api_user_name':api_user_name,
        'api_user_password':api_user_password}

r = requests.post(url, data=body)

print(r.text)