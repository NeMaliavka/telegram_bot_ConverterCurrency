import telebot
import config
import exceptions as exp

token = config.token
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Добро пожаловать в бот-конвертер валют!
Для получения нужного результат введите следующую информацию:
<название валюты, в которую хотите перевести> <название висходной алюты> <количество>

Для получения списка доступных валют: /values'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in config.currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split()
        if len(values) != 3:
            eror = '''Проверьте передаваемую информацию.
    В сообщении должно быть только 3 элемента:
    В какой валюте необходимо получить стоимость
    Какую именно валюту переводим
    Количество'''
            raise exp.ConvertError(eror)
        else:
            fsym, tsyms, count = values
            result = config.APIclass.get_price(fsym, tsyms, count)
    except exp.ConvertError as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось выполнить команду, попробуйте повторить свой запрос позднее\n{e}')
    else:
        text = f'Конвертируем {fsym} в {tsyms} в кол-ве {count} шт. Получаем : {result}'
        bot.send_message(message.chat.id, text)


# @bot.message_handler(content_types=['photo'])
# def func(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)
