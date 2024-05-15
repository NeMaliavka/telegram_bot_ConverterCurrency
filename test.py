import requests
import json

currency = {'биткоин': 'BTC',
            'эфирум': 'ETH',
            'доллар': 'USD',
            'рубли': 'RUB'}

text = input()
fsym, tsyms, count = text.split()
r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currency[fsym]}&tsyms={currency[tsyms]}')
result = json.loads(r.content)[currency[tsyms]]
print(result, type(result))
