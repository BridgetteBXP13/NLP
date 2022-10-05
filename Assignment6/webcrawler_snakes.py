# Tera Parish       txp200011
# Bridgette Bryant  bmb180001

from bs4 import BeautifulSoup
import requests

def crawl(starter_url):
    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data, features="lxml")

    counter = 0
    # write urls to a file
    with open('snake_urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            #print(link_str)
            if 'Snake' in link_str or 'snake' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    #print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

if __name__== '__main__':
    starter_url = 'https://www.nationalgeographic.com/animals/reptiles/facts/snakes-1'

    # Call the crawler for the starting url
    crawl(starter_url)

    que = []

    with open('snake_urls.txt', 'r') as file:
        urls = file.read().splitlines()
    for u in urls:
        #while len(que) <= 15:
            #que.append(u)
        print(u)
        crawl(u)


    # end of program
    print("end of crawler")