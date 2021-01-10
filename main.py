import requests, time, telebot, config
from bs4 import BeautifulSoup

from telebot import types

bot = telebot.TeleBot(config.Token)
global prov, prov_d, url
prov = 0
prov_d = 0
url = ''
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(content_types=['text'])
def main2(message):
    message = message
    global prov, prov_d, url
    if message.chat.type == 'private':
        if 'URL - ' in message.text and 'https://rule34.xxx/index.php' in message.text:
            prov = 1
            link2 = message.text
            links = link2.split()
            url = links[2]

        elif 'page - ' in message.text and prov == 1:
            page = message.text
            pages = page.split()
            page1 = pages[2]
            prov_d = 1

        if prov_d ==1 and prov == 1:
            print(page1 +' '+ url)
            config.links(url, int(page1), bot, message)

            prov = 0
            prov_d = 0

            bot.send_message(message.chat.id, 'Done!')


if __name__ == '__main__':
    bot.infinity_polling()
