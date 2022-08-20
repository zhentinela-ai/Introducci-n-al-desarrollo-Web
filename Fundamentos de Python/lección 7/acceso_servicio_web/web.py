import requests

# Accede a coinmarketcap.com y obtiene la información de los últimos cambios de criptomonedas
url = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b9f8b8c4-f8f4-4f0f-b8e2-b9f8b8c4f8f4'
}

parameters = {
  'limit': 10,
  'convert': 'USD',
  'sort': 'volume_24h'
}

result = requests.get(url, headers=headers, params=parameters)
cripto_lastest = result.json()['data']

if (cripto_lastest):
  for cripto in cripto_lastest:
    print(cripto['name'], ':', cripto['price_usd'])