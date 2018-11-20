
import configparser
import requests
import json
import fetchPasteWithKey as f
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']

limit='100'
#lang='yaml'

#url='https://scrape.pastebin.com/api_scraping.php?limit='+limit+'&lang='+lang
url='https://scrape.pastebin.com/api_scraping.php?limit='+limit

body={'api_dev_key':api_dev_key,
      'api_user_key':api_user_key
}

r = requests.post(url,data=body)
print(r.text)

ids = json.loads(r.text)

sleep = 1.2

for paste in ids:
    try:
        f.fetchAndStorePastes(paste.get('key'),sleep)
    except ClientError:
        print(ClientError.response)
        continue




