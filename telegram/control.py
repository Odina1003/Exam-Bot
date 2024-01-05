import telebot
import requests

BOT_TOKEN = '6501703401:AAFFa6q9GH4SX2v7N6KsXcxQkWne6D4AB_I'
LINK = 'https://uz.wikipedia.org/wiki/'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def greeting(message):
    bot.reply_to(message, 'Botga xush kelibsiz!')

@bot.message_handler(commands=['info'])
def informations(message):
    info = message.text[6:]
    url = LINK.format(info)
    response = requests.get(url)
    bot.send_message(message.chat.id, response.json())