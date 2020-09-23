import requests
from bs4 import BeautifulSoup
import time

class search_engines:

    def __init__(self,search,num):
        self.search = search
        self.num = str(int(num)+5)
        self.HEADER = '\033[92m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def google_search(self):
        url = "https://google.com/search?q="+"+".join(self.search.split())+"&num="+self.num
        print(url)
        data = requests.get(url,headers={'User-Agent': 'Mozilla/76.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        soup = BeautifulSoup(data.content,"html.parser")
        web_links = soup.find_all("div",{"class":"rc"})
        for web_link in web_links:
            for link,text,title in zip(web_link.find_all("div",{"class":"r"}),web_link.find_all("span",{"class":"st"}),web_link.find_all("h3",{"class":"LC20lb DKV0Md"})):
                print('\n'+self.HEADER+title.text+self.ENDC)
                print(self.UNDERLINE+link.find('a',href=True).get('href')+self.ENDC)
                print(text.text)
        time.sleep(5)

    def bing_search(self):
        url = "https://www.bing.com/search?q="+"+".join(self.search.split())+"&count="+self.num
        data = requests.get(url,headers={'User-Agent': 'Mozilla/76.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        soup = BeautifulSoup(data.content,"html.parser")
        web_links = soup.find_all('li',{'class':'b_algo'})
        for web_link in web_links:
            for title in web_link.find('h2'):
                print('\n'+self.HEADER+title.text+self.ENDC)
                print(self.UNDERLINE+title.get('href')+self.ENDC)
        time.sleep(5)