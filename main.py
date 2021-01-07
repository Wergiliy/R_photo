from bs4 import BeautifulSoup
import  requests


j = 1


HEADERS = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
            }
def first_step(intr, url, HEADERS, j, bolPrint):
    result=[]
    try:

        for i in range(intr):
            URL = url+str(i*42)


        response =requests.get(URL,  HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('span', 'thumb')
        comps = []
        try:
            for item in items:
                comps.append({
                    'link': item.find('a').get('href')
                })
                if bolPrint == 1:
                    print('(I)Completed ' +str(j))
                j+=1



            for comp in comps:
            #    f.write('https://rule34.xxx/' + comp['link']+'\n')
                result.append('https://rule34.xxx/' + comp['link'])
        except:
            print('Something wrong.(I:2)')
    except:
        print('Something wrong.(I:1)')
    return result


def second_step(HEADERS, bolPrint, result):
    links = []
    res = []
    global iterred
    iterred = 0
    global tags
    tags=[]

    for i in range(len(result)):
        try:
            CC=[]
            URL = result[i]

            response = requests.get(URL, HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            videos = soup.findAll('source')
            items = soup.findAll('img')
            comps = []
            compes = []

            for item in items:
                compes.append(item.get('src'))
                CC.append(item.get('alt'))
            for video in videos:
                compes.append(video.get('src'))
                CC.append((video.get('alt')))

            firt = compes[2]
            res.append(firt)

            th = True
            while th:
                if 'https://rule34.xxx/images/shirt2.jpg' in res:
                    th = True
                else:
                    th = False
                    continue
                res.remove('https://rule34.xxx/images/shirt2.jpg')

            iterred += 1
            CC.pop(0)
            CC.pop(2)
            CC.pop(0)
            tags.append(CC[0]) #TAGs for TG




            if bolPrint == 1:
                print('(II)Completed ' + str(iterred)+'/'+str(len(result)))
        except:
            print('Something wrong.')
            continue
    for i in range(len(tags)):
        tags[i]=tags[i].split(' ')
    for i in range(len(tags)):
        for j in range(len(tags[i])):
            tags[i][j]='#'+tags[i][j]
    print(tags)
    return res





def final(bolPrint, rest1):

    global iter
    iter = 1
    #try:

    links = rest1
    for i in range(len(links)):
        try:
            if 'jpg' in links[i]:
                name = str(i) + '.jpg'
            elif 'jpeg' in links[i]:
                name = str(i) + '.jpeg'
            elif 'png' in links[i]:
                name = str(i) + '.png'
            elif 'gif' in links[i]:
                name = str(i) + '.gif'
            elif 'mp4' in links[i]:
                name = str(i) + '.mp4'
            url = links[i]
            r = requests.get(url)
            if bolPrint==1:
                print('(III)Complete ' + str(iter)+'/'+str(iterred-1))
            iter += 1
            with open(name, 'bw') as f:

                f.write(r.content)
        except:
            print('Something wrong.')
            continue
if __name__ == '__main__':
    url = input('Send link (from r34) => ')+'&pid='
    global bolPrint
    bolPrint = int(input('Show statistic? (1-yes; 0-no) => '))
    intr = int(input('How match pages => '))
    if bolPrint == 1:
        print('Step I:')
    rest=first_step(intr, url, HEADERS, j, bolPrint)
    if bolPrint ==1:
        print('Step II:')
    rest1=second_step(HEADERS, bolPrint, rest)
    if bolPrint == 1:
        print('Step III: ')
    final(bolPrint, rest1)
    print('Done! ' + str(iter-1) +' media file`s has been downloaded.')