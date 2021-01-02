from bs4 import BeautifulSoup
import  requests
import os

j = 1


HEADERS = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
            }
def first_step(intr, url, HEADERS, j, bolPrint):
    with open('txt\links.txt', 'w') as f:
        for i in range(intr):
            URL = url+str(i*42)


            response =requests.get(URL,  HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('span', 'thumb')
            comps = []

            for item in items:
                comps.append({
                    'link': item.find('a').get('href')
                })
                if bolPrint == 1:
                    print('(I)Completed ' +str(j))
                j+=1



            for comp in comps:
                f.write('https://rule34.xxx/' + comp['link']+'\n')

def second_step(HEADERS, bolPrint):
    shirt = True
    links = []
    res = []
    global iterred
    iterred = 1
    with open('txt\links.txt', 'r') as f:
        links.append(f.read().split('\n'))
    with open('txt\links1.txt', 'w') as f:
        for i in range(len(links)):
            for j in range(len(links[i]) - 1):
                URL = links[i][j]


                response = requests.get(URL, HEADERS)
                soup = BeautifulSoup(response.content, 'html.parser')
                #videos = soup.findAll('video')
                videos = soup.findAll('source')
                items = soup.findAll('img')
                comps = []
                compes = []

                for item in items:
                    #f.write(item.get('src') + '\n')
                    compes.append(
                        item.get('src')
                    )
                for video in videos:
                    f.write(video.get('src')+'\n')
                    #comps.append(
                    #    video.get('src')
                    #)
                firt = compes[2]
                res.append(firt)
                while shirt:
                    for i in range(len(res)):
                        if res[i] =='https://rule34.xxx/images/shirt2.jpg':
                            res.remove('https://rule34.xxx/images/shirt2.jpg')
                        else: shirt =False
                if bolPrint == 1:
                    print('(II)Completed ' + str(iterred)+'/'+str(len(links[i])-1) )
                iterred += 1


            for compl in res:
                f.write(compl +'\n')
    print(res)

def final(bolPrint):
    links = []
    global iter
    iter = 1

    with open('txt\links1.txt', 'r') as f:
        links.append(f.read().split('\n'))
        links = links[0]
    links.pop(-1)

    for i in range(len(links)):
        if 'jpg' in links[i]:
            name = str(iter) + '.jpg'
        elif 'jpeg' in links[i]:
            name = str(iter) + '.jpeg'
        elif 'png' in links[i]:
            name = str(iter) + '.png'
        elif 'gif' in links[i]:
            name = str(iter) + '.gif'
        elif 'mp4' in links[i]:
            name = str(iter) + '.mp4'
        url = links[i]
        r = requests.get(url)
        if bolPrint==1:
            print('(III)Complete ' + str(iter)+'/'+str(iterred-1))
        iter += 1
        with open(name, 'bw') as f:

            f.write(r.content)
if __name__ == '__main__':
    url = input('Send link (from r34) => ')+'&pid='
    global bolPrint
    bolPrint = int(input('Show statistic? (1-yes; 0-no) => '))
    intr = int(input('How match pages => '))
    if bolPrint == 1:
        print('Step I:')
    first_step(intr, url, HEADERS, j, bolPrint)
    if bolPrint ==1:
        print('Step II:')
    second_step(HEADERS, bolPrint)
    if bolPrint == 1:
        print('Step III: ')
    final(bolPrint)
    print('Done! ' + str(iter-1) +' media file`s has been downloaded.')