import requests as req
from os import getcwd, mkdir, listdir
from os.path import isdir
from random import randint
from time import sleep
import json
from bs4 import BeautifulSoup
class Get_A_Page:
    def __init__(self, city,agent=None,proxy=None):
        self.proxy=proxy
        self.city=city
        self.agent=agent
        self.url = 'https://www.avito.ru/{0}/kvartiry'.format(self.city)
        self.headers={'User-Agent':agent}
        self.url_param='?context=&p='
        self.html_path='{0}\\htmls'.format(getcwd())
    def get_html(self,number_page=1):
        if isdir(self.html_path) == False:
            mkdir(self.html_path)
        with open('{0}\\{1}page{2}.html'.format(self.html_path,self.city,str(number_page)), 'w', encoding='utf-8') as html_file:
            response=req.get('{0}{1}{2}'.format(self.url,
                                                    self.url_param,
                                                    str(number_page)),headers=self.headers)
            response.encoding='utf-8'
            html_file.write(response.text)
            sleep(randint(15,30))
class GetData:
    def __init__(self, city):
        self.city=city
        self.pattern='/{0}/kvartiry/'.format(self.city)
        self.cute='^^'
    def search(self,filename):
        with open(filename, 'r',encoding='utf-8') as html_file:
            html_text=html_file.read()
            bs=BeautifulSoup(html_text, 'lxml')
            del html_text
            info_list,price_list=[],[] #i like a fuck with to the list's lol            
            list(price_list.append(price.text.replace('\xa0', '').replace('₽', '')) for price in bs.findAll('strong', class_='styles-module-root-bLKnd'))
            for info in bs.findAll('div', class_='iva-item-titleStep-pdebR'):
                info_list.append([info.text.replace('\xa0', '')])
            del price_list[0],price_list[-1] 
            fixed_list=[]
            for x in info_list:
                fixed_list.append(Helpers().normalize_list(x))
            urls,links=[],[]
            for href in bs.findAll('a', class_='styles-module-root-YeOVk styles-module-root_noVisited-MpiGq'):
                link=href.attrs.get('href')
                if link=='' or link is None:
                    continue
                else:
                    links.append(link)
            for x in links:
                temp=x[0:len(self.pattern)]
                if temp==self.pattern:
                    print(True)
                    urls.append(x)
            del bs
            return fixed_list, price_list,urls           
class Helpers:
    def normalize_list(self, ur_list):
        ur_list=''.join(ur_list)
        ur_list=ur_list.split(',')
        #info about of apartaments, in general, sait Avito giving a data that are desirible for de parsing yeah
        normalize_list=[]
        normalize_list.append(ur_list[0])
        normalize_list.append(ur_list[-1])
        del ur_list[0], ur_list[-1]
        ur_list[0]=ur_list[0]+'.'
        normalize_list.append(''.join(ur_list))
        return normalize_list
