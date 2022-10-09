# Bridgette Bryant  bmb180001

from bs4 import BeautifulSoup
import requests

def crawl(count, que, file):
    #print("In crawl")
    #print("count: ", count)
    # If we have reached our maximum count, return
    if count == 300:
        return
    if len(que) == 0:
        return

    r = requests.get(que.pop())
    data = r.text
    soup = BeautifulSoup(data, features="lxml")

    # write urls to a file

    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        print(link_str)
        if 'Snake' in link_str or 'snake' in link_str:
            if link_str.startswith('/url?q='):
                link_str = link_str[7:]
                #print('MOD:', link_str)
            if '&' in link_str:
                i = link_str.find('&')
                link_str = link_str[:i]
            if link_str.startswith('http') and 'linkedin' not in link_str and 'instagram' not in link_str and 'facebook' not in link_str and 'robot' not in link_str and 'twitter' not in link_str and 'bite' not in link_str and 'bitten' not in link_str and 'killed' not in link_str and 'google' not in link_str and 'buzzfeed' not in link_str and link_str not in que:
                file.write(link_str + '\n')
                que.append(link_str)
                print("saved: ", link_str)
                count += 1
                # If we have reached our maximum count, return
                if count == 300:
                    return
                #print("count 2: ", count)
                crawl(count, que, file)
                #print("count 3: ", count)
                # If we have reached our maximum count, return
                if count == 300:
                    return
    return


if __name__ == '__main__':

    starter_url = 'https://www.nationalgeographic.com/animals/reptiles/facts/snakes-1'
    que = []
    count = 0
    que.append(starter_url)

    with open('snake_urls.txt', 'w') as file:
        file.write(starter_url + '\n')
        crawl(count, que, file)


    urls_found = set()

    with open('snake_urls.txt', 'r') as file:
        urls = file.read().splitlines()
    for u in urls:
        print(u)
        urls_found.add(u)
    print(urls_found)
    print("number of urls: ", len(urls_found))


    # end of program
    print("end of crawler")