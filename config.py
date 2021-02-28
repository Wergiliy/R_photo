import requests, telebot
from bs4 import BeautifulSoup
Token = '1558899195:AAE0IZdAksZ-iHQ0KKoGBYtTkYyEJRQ2LWE'


def links(url, pages, bot, message):
    bot = bot
    message = message
    URLS = []
    try:
        global j
        j = 1
        for i in range(pages):
            link = url +'&pid='+str(i*42)

            responce = requests.get(link)
            soup = BeautifulSoup(responce.content, 'html.parser')
            items = soup.findAll('span', 'thumb')

            try:
                for item in items:
                    URLS.append('https://rule34.xxx/'+item.find('a').get('href'))
                    print('(I) Complete => ' + str(j))
                    j+=1
            except Exception as e:
                print('I(2)')
                print(e)

    except Exception as e:
        print('I(1)')
        print(e)
    media(URLS, bot, message)

def media(urls, bot, message):



    try:
        for k in range(len(urls)):
            tags = []
            tstr=''
            res = ''
            im = []
            responce = requests.get(urls[k])
            soup = BeautifulSoup(responce.content, 'html.parser')
            tgs = soup.find('ul', {'id':'tag-sidebar'})

            tgs1 = tgs.findAll('li', {'class':'tag-type-copyright tag'})
            tgs2 = tgs.findAll('li', {'class':'tag-type-character tag'})
            tgs3 = tgs.findAll('li', {'class':'tag-type-general tag'})
            video = soup.findAll('source')
            imgs = soup.findAll('img')
            for item in imgs:
                im.append (item.get('src'))

            for vid in  video:
                res = vid.get('src')
            for tag in tgs1:
                tags.append(tag.find('a').get_text())
            for tag in tgs2:
                tags.append(tag.find('a').get_text())
            for tag in tgs3:
                tags.append(tag.find('a').get_text())

            if im[2] != 'https://rule34.xxx/images/shirt2.jpg':
                res = im[2]
            try:


                r = requests.get(res)
                global  j
                for tag in tags:

                    tstr +='#'+tag.replace(' ','_')+' '


                if 'jpg' in res:
                    bot.send_photo(message.chat.id, res, caption=tstr)
                elif 'jpeg' in res:
                    bot.send_photo(message.chat.id, res, caption=tstr)
                elif 'png' in res:
                    bot.send_photo(message.chat.id, res, caption=tstr)
                elif 'gif' in res:
                    bot.send_video(message.chat.id, res, caption=tstr)
                elif 'mp4' in res:
                    bot.send_video(message.chat.id, res, caption=tstr)
                bot.send_document(message.chat.id, res)
                print('(II)Complete ' + str(k + 1) + '/' + str(j - 1) + ' - ' + urls[k])
            except Exception as e:
                print('II(2)')
                print(e)



    except Exception as e:
        print('II(1)')
        print(e)