from bs4 import BeautifulSoup
import  requests

links = []
res= []
iterred = 1
with open('links.txt', 'r') as f:
    links.append(f.read().split('\n'))
with open('links1.txt', 'w') as f:
    for i in range(len(links)):
        for j in range(len(links[i])-1):
            URL = links[i][j]
            HEADERS = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
            }

            response =requests.get(URL,  HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('img')
            comps = []

            for item in items:
                comps.append(
                     item.get('src')
                )
            firt = comps[2]
            res.append(firt)
            print('Completed '+ str(iterred) +'/247')
            iterred+=1

        for comp in res:
            f.write(comp+'\n')