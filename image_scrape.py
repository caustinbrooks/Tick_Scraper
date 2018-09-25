# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:43:54 2018

@author: Austin
"""
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import pandas as pd
import os



def image_request(url):
    url_split = url.split('/')
    directory = "G:\\My Drive\\" +"\\" + url_split[3] +"\\"+ url_split[4]+"\\"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
        r = requests.get(url)
        
        #directory = os.getcwd() + "\\" + url_split[3] +"\\"+ url_split[4]+"\\"
        directory = "G:\\My Drive\\" +"\\" + url_split[3] +"\\"+ url_split[4]+"\\"
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        #pprint(r.text)
        soup = bs(r.text,'lxml')
        
        image_links = soup.find_all('a',{'class':'btn btn-primary'})
        for link in image_links:
            image = link["href"] 
            path_and_name =  os.path.split(image)
            image_name = path_and_name[1]
            if image_name[:-4] != '.jpg':
                image_name += '.jpg'
            if not os.path.exists(directory + image_name):    
                r2 = requests.get(image)
            
                with open(directory + image_name, "wb") as f:
                        f.write(r2.content)
                print("Completed: " + url)
    else:
        print("Skipped: " +url)

df = pd.read_csv('cleaned_tick_data.csv', encoding='utf-8')
count = 0
for url in df["URL"]:
    #print(url)
    image_request(url)#'https://www.tickreport.com/report/55483')#'https://www.tickreport.com/report/6251')
    count += 1

print("Completed: " + str(count) + " Image Downloads")