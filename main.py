import requests, time, telebot, config
from datetime import  datetime
from bs4 import BeautifulSoup

from telebot import types

bot = telebot.TeleBot(config.Token)
global prov, prov_d, url, tagMark1, tagss
prov = 0
prov_d = 0
tagMark1 = 0
url = ''
tagss = ''
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(content_types=['text'])
def main2(message):
    message = message
    global prov, prov_d, url, tagMark1, tagss
    if message.chat.type == 'private':
        if 'URL - ' in message.text and 'https://rule34.xxx/index.php' in message.text:
            prov = 1
            link2 = message.text
            links = link2.split()
            url = links[2]


        elif 'tags - ' in message.text:
            tagsz = message.text
            tags = tagsz.split()
            tags.pop(0)
            tags.pop(0)
            tagss = ''
            for i in range(len(tags)):
                tagss += tags[i]+' '
            bot.send_message(message.chat.id,tagss.replace('#',''))
            global tagMark1
            tagMark1 = 1
            print(tagMark1)
            print(prov_d)
        elif 'page - ' in message.text:
            page = message.text
            pages = page.split()
            page1 = pages[2]
            prov_d = 1
            print(page1)

        if prov_d ==1 and prov == 1 and tagMark1 ==0:
            print(page1 +' '+ url)
            config.links(url, int(page1), bot, message)

            prov = 0
            prov_d = 0

            bot.send_message(message.chat.id, 'Done!')
        elif tagMark1 == 1 and prov_d == 1:
            print('work')
            tagss= tagss.replace(' ','+')
            tagss= tagss.replace('#','')
            print(tagss)

            url = 'https://rule34.xxx/index.php?page=post&s=list&tags='+tagss
            #with open('logs.txt', 'w+') as f:
            #    date =str( datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
            #    print(type(date))
            #    f.writelines('['+date+'] - ' + message.chat.id +' :'+ url)
            print(page1 + ' ' + url)
            config.links(url, int(page1), bot, message)

            tagMark1 = 0
            prov_d = 0


if __name__ == '__main__':
    bot.infinity_polling()
