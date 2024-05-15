import config


class ConvertError(Exception):
    pass


class CriptoConvertor:
    @staticmethod
    def convert(fsym: str, tsyms: str, count: str):
        if fsym not in config.currency or tsyms not in config.currency:
            error = '''Проверьте написание валют, 
    возможно, Вы опечатались, или же ввели валюту, которую данныей бот обработать не может.'''
            raise ConvertError(error)



