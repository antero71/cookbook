
import configparser
import requests

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']

limit='10'
lang='kotlin'

url='https://scrape.pastebin.com/api_scraping.php?limit='+limit+'&lang='+lang

body={'api_dev_key':api_dev_key,
      'api_user_key':api_user_key
}

r = requests.post(url,data=body)
print(r.text)