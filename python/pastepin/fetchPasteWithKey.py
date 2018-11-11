import configparser
import requests
import boto3
import json

def removeEmptyItems(data):
    """This method removes a empty items from a dictionary"""
    removeKeys = []

    for key, value in data.items():
        if value == "":
            removeKeys.append(key)

    for key in removeKeys:
        data.pop(key)

    return data



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

data = json.loads(r.text)


data = removeEmptyItems(data[0])

data['raw_data'] = raw_data.text

print(data)

import database.databaseOperations as oper

oper.storeData(data)



