
import configparser
import requests
import json
import fetchPasteWithKey as f

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']

limit='10'
#lang='yaml'

#url='https://scrape.pastebin.com/api_scraping.php?limit='+limit+'&lang='+lang
url='https://scrape.pastebin.com/api_scraping.php?limit='+limit

body={'api_dev_key':api_dev_key,
      'api_user_key':api_user_key
}

r = requests.post(url,data=body)
print(r.text)

ids = json.loads(r.text)

for paste in ids:
    f.fetchAndStorePastes(paste.get('key'))





