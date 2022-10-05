# Tera Parish       txp200011
# Bridgette Bryant  bmb180001

from bs4 import BeautifulSoup
import requests

if __name__== '__main__':
    starter_url = 'https://www.bbc.com/news/world-europe-56720589.amp'
    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data, features="lxml")

    counter = 0
    # write urls to a file
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            print(link_str)
            if 'Gilligan' in link_str or 'gilligan' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

    # end of program
    print("end of crawler")

    # end of program
    print("end of crawler")