import  requests
links = []
iter = 1

with open('links1.txt', 'r') as f:
    links.append(f.read().split('\n'))
    links = links[0]
links.pop(-1)

for i in range(len(links)):
    if 'jpg' in links[i]:
        name = str(iter)+'.jpg'
    elif 'jpeg' in links[i]:
        name = str(iter)+'.jpeg'
    elif 'png'in links[i]:
        name = str(iter) + '.png'
    elif 'gif' in links[i]:
        name = str(iter) + '.gif'
    url = links[i]
    r = requests.get(url)
    print('Complite ' +str(iter)+'/247')
    iter+=1
    with open(name, 'bw') as f :

        f.write(r.content)
