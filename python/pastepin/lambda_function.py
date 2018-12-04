
import configparser
import requests
import json
import fetchPasteWithKey as f
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read('.env')

api_dev_key = config['KEYS']['api_dev_key']
api_user_key = config['KEYS']['api_user_key']
limit = config['KEYS']['limit']
""" limit: How many pastes you want fetch
   pastebin defaul is 50 and maximum number are 250."""



def getData(limit):
    """ Find the latest pastes from pastebin """

    # If you want fetch a specific format
    # more information from here https://pastebin.com/api#5
    # lang='yaml'

    # url='https://scrape.pastebin.com/api_scraping.php?limit='+limit+'&lang='+lang
    url = 'https://scrape.pastebin.com/api_scraping.php?limit=' + limit
    body = {'api_dev_key': api_dev_key,
            'api_user_key': api_user_key
    }
    r = requests.post(url,data=body)
    return json.loads(r.text)

def lambda_handler(event, context):

    sleep = 1.2
    pastes = getData(limit)

    for paste in pastes:
        try:
            f.fetchAndStorePastes(paste, sleep)
        except ClientError:
            print(ClientError.response)
            continue


    return {
        'statusCode': 200,
        'body': json.dumps('Pastebin search success!')
    }



