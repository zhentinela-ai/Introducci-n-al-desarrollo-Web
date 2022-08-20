from time import sleep
import mysql.connector
import requests
from datetime import datetime

class Config:
  def __init__(self):
    self.url = "https://pro-api.coinmarjetcap.com/v1/cryptocurrency/listings/latest"

    self.headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '',
    }

    self.params = {
      'limit': '50',
      'convert': 'USD',
      'sort': 'market_cap'
    }

    self.database_conn = {
      'host': 'localhost',
      'user': 'root',
      'password': '',
      'database': '',
    }

conf = Config()

mydb = mysql.connector.connect(
  host=conf.database_conn['host'],
  user=conf.database_conn['user'],
  password=conf.database_conn['password'],
  database=conf.database_conn['database']
)
mycursor = mydb.cursor()

while True:
  coins = get_currency(conf.url, conf.headers, conf.params)