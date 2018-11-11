
import configparser
import requests
import json

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


