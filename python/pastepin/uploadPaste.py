# This is a simple pastebin paste program
#
# It prints url where you can find newly created paste
#
api_paste_code = '<html><body><b>This is a test</b></body></html>'
api_paste_name = 'my title'
api_paste_private=2
api_paste_expire_date = '10M'
api_paste_format = 'html4strict'

import configparser

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']


import requests

body = { 'api_dev_key':api_dev_key,
         'api_option': 'paste',
         'api_user_key':api_user_key,
         'api_paste_code':api_paste_code,
         'api_paste_format':api_paste_format,
         'api_paste_expire_date':api_paste_expire_date,
         'api_paste_private':api_paste_private,
         'api_paste_name':api_paste_name}

r = requests.post('https://pastebin.com/api/api_post.php',data=body)

print(r.text)