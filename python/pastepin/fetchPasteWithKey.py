import configparser
import requests
import boto3
import json





config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']
api_paste_key='PASTE_KEY'

url_raw = 'https://scrape.pastebin.com/api_scrape_item.php?i='+api_paste_key

raw_data = requests.post(url_raw)

url_metadata = 'https://scrape.pastebin.com/api_scrape_item_meta.php?i='+api_paste_key

r = requests.post(url_metadata)
print('Post metadata')
print(r.text)

session = boto3.Session(profile_name='pastebin_caller',region_name='eu-west-1')



data = json.loads(r.text)

removeKeys=[]

for key, value in data[0].items():
    if value == "":
        removeKeys.append(key)

for key in removeKeys:
    data[0].pop(key)

data[0]['raw_data'] = raw_data.text

print(data[0])

import database.databaseOperations as oper

oper.storeData(data[0])
