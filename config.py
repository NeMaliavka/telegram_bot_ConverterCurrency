import requests
import  exceptions as exp
import json
token = '6615591356:AAFphtgLE5mAFGcw3GNoTTGKKfsyQ-0gDHw'

currency = {'биткоин': 'BTC',
            'эфирум': 'ETH',
            'доллар': 'USD',
            'рубли': 'RUB'}


class APIclass:
    @staticmethod
    def get_price(fsym: str, tsyms: str, count):
        if fsym == tsyms:
            error = f'Не получается сконвертировать {fsym} в {tsyms}'
            raise exp.ConvertError(error)
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currency[fsym]}&tsyms={currency[tsyms]}')
            count = int(count)
            total_base = json.loads(r.content)[currency[tsyms]]
            result = round(count * total_base, 2)
        except ValueError:
            raise exp.ConvertError(f'Не удалось обработать количество {count}')
        except Exception as e:
            raise exp.ConvertError(f'Не удалось выполнить команду, попробуйте повторить свой запрос позднее\n{e}')
        else:
            return result


