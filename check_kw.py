from bs4 import BeautifulSoup as beautifulsoup
import requests

class Scrapping():
    def __init__(self,dom,keywords):
        self.dom = dom
        self.keywords = keywords

    def make_soup(self,kw,start):
        self.kw = kw
        self.r = requests.get(f'https://www.google.com/search?q={self.kw}&start={start}')
        self.soup = beautifulsoup(self.r.text,'html.parser')
        self.div_main = self.soup.find('div',{'id':'main'})
        
        self.d_link = self.div_main.find_all('div',class_='ZINbbc xpd O9g5cc uUPGi')
        return self.d_link
    
    def check_keyword(self):
        self.start = 0
        self.count = 0
        self.searching = True
        for words in self.keywords:
            while self.searching:
                for link in self.make_soup(words,self.start):
                    if link.div and link.div.a:
                        self.count += 1
                        if self.find_dom(self.dom,link.div.a['href']):
                            return int(self.count)
                            self.searching= False
                            self.count=0
                            self.start=0
                            break
                if self.count > 99:
                    return self.count
                    self.count=0
                    self.start=0
                    break

                self.start += 10
            self.searching = True

    def find_dom(self,link_s,link_r):
        self.link_r = str(link_r)
        try:
            if link_r.index(link_s) > 0:
                return True             
        except:
            return False
