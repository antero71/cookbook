import configparser
import requests

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']
api_paste_key='PASTE_KEY_HERE'

url_raw = 'https://scrape.pastebin.com/api_scrape_item.php?i='+api_paste_key

r = requests.post(url_raw)
print('raw paste')
print(r.text)

url_metadata = 'https://scrape.pastebin.com/api_scrape_item_meta.php?i='+api_paste_key

r = requests.post(url_metadata)
print('Post metadata')
print(r.text)