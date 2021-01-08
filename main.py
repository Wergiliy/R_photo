import  telebot
import defs
import requests
from bs4 import BeautifulSoup
from telebot import types
bot = telebot.TeleBot('1558899195:AAE0IZdAksZ-iHQ0KKoGBYtTkYyEJRQ2LWE')
global interf, link, pages

HEADERS = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
            }


@bot.message_handler(commands=['link','start', 'pages'])
def links(message):
    global interf, link, pages
    link = ''
    pages = 0
    interf = 0
    if message.text=='/link':
        bot.send_message(message.chat.id, 'link')
    elif message.text == '/pages':
        bot.send_message(message.chat.id, 'pages')
    #bot.send_message(message.chat.id, 'working')

@bot.message_handler(content_types=['text'])
def repeat(message):
    global interf, link, pages

    if message.chat.type == 'private' :
        if 'http' in message.text: #Добавить проверку на сайт от дураков
            print(message.text)

            interf=1
            link = message.text
            print(link)
            bot.send_message(message.chat.id, 'Now, pages')
        elif interf == 1 :
            pages = int(message.text)
            interf=2
            print(message.text)
        elif interf ==2 and message.text == 'start':
            result = []
            j=1
            try:

                for i in range(pages):
                    URL = link +'&pid='+ str(i * 42)

                    response = requests.get(URL, HEADERS)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    items = soup.findAll('span', 'thumb')
                    comps = []
                    try:
                        for item in items:
                            comps.append({
                                'link': item.find('a').get('href')
                            })

                            print('(I)Completed ' + str(j))
                            j += 1

                        for comp in comps:
                            #    f.write('https://rule34.xxx/' + comp['link']+'\n')
                            result.append('https://rule34.xxx/' + comp['link'])
                    except:
                        print('Something wrong.(I:2)')
            except:
                print('Something wrong.(I:1)')
            res = defs.second_step(HEADERS, result)
            for k in range(len(res)):
                bot.send_photo(message.chat.id, defs.final(res[k], k))


if __name__ == '__main__':
    bot.infinity_polling()