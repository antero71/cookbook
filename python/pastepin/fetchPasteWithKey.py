import configparser
import requests
import boto3
import json
import time
import database.databaseOperations as oper
from s3.storeFileToS3 import storeDataToS3

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
#api_paste_key='PASTE_KEY'


def fetchAndStorePastes(paste,sleep):
    api_paste_key = paste.get("key")

    time.sleep(sleep)

    url_raw = 'https://scrape.pastebin.com/api_scrape_item.php?i='+api_paste_key

    raw_data = requests.post(url_raw)

    #url_metadata = 'https://scrape.pastebin.com/api_scrape_item_meta.php?i='+api_paste_key

    #r = requests.post(url_metadata)
    #print('Post metadata')
    #print(r.text)

    ##data = json.loads(r.text)

    ##data = removeEmptyItems(data[0])
    data = removeEmptyItems(paste)

    name=data.get("key")
    name+='.txt'

    storeDataToS3(name,raw_data.text)

    print(data)

    oper.storeData(data)





