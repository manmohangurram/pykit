import requests
from bs4 import BeautifulSoup
import os

def clear_screen():
    os.system('clear')

def currency_convert(quantity=1,initial='INR',to='USD'):
    url = "https://currency-exchange.p.rapidapi.com/exchange"
    querystring = {"q":"1.0","from":initial,"to":to}
    headers = {
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
    'x-rapidapi-key': "789d22491amsh9cf6fe5ac3b3cf8p195e80jsn0b807e6d418c"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

class search_engines:

    def __init__(self,search,num):
        self.search = search
        self.num = num
        self.HEADER = '\033[92m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def google_search(self):
        url = "https://google.com/search?q="+"+".join(self.search.split())+"&num="+self.num
        data = requests.get(url,headers={'User-Agent': 'Mozilla/76.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        soup = BeautifulSoup(data.content,"html.parser")
        web_links = soup.find_all("div",{"class":"rc"})
        for web_link in web_links:
            for link,text,title in zip(web_link.find_all("div",{"class":"r"}),web_link.find_all("span",{"class":"st"}),web_link.find_all("h3",{"class":"LC20lb DKV0Md"})):
                print('\n'+self.HEADER+title.text+self.ENDC)
                print(self.UNDERLINE+link.find('a',href=True).get('href')+self.ENDC)
                print(text.text)

    def bing_search(self):
        url = "https://www.bing.com/search?q="+"+".join(self.search.split())+"&count="+self.num
        data = requests.get(url,headers={'User-Agent': 'Mozilla/76.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        soup = BeautifulSoup(data.content,"html.parser")
        web_links = soup.find_all('li',{'class':'b_algo'})
        for web_link in web_links:
            for title,link,content in zip(web_link.find('h2'),web_link.find('cite'),web_link.find('p')):
                print(title.text)
                print(link.text)
                print(content.text+'\n')

if __name__ == "__main__":
    clear_screen()
    print('1.Search\n2.Currency Converter')
    choice = input('Select your choice : ')
    if choice=='1':
        clear_screen()
        search = input('What do you like to search : ')
        num = input('Enter No.of results (default = 10 ) : ')
        s = search_engines(search,num)
        print('1.Google\n2.Bing')
        choice = input('Selet prefered search engine : ')
        if choice == '1': s.google_search()
        else: s.bing_search()
    else:
        print(' ')


