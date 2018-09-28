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
import glob
#WARNING DO NOT RUN without Adequate Storage, Bandwidth, and a High Data Limit
#A full year (2018) download is estimated at 200 GB

def html_request(url):
    url_split = url.split('/')
    directory = "G:\\My Drive\\" +"\\" + url_split[3] +"\\"+ url_split[4]+"\\"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
        r = requests.get(url)
        
        #directory = os.getcwd() + "\\" + url_split[3] +"\\"+ url_split[4]+"\\"
        html_file = "G:\\My Drive\\" +"\\" + url_split[3] +"\\"+ url_split[4]+"\\"+url_split[4]+".html"
        if not os.path.exists(html_file):
            with open(html_file, "w") as f_html:
                        f_html.write(r.text)
            print("Wrote " + url_split[4]+".html" )
        #pprint(r.text)
#        soup = bs(r.text,'lxml')
#        
#        image_links = soup.find_all('a',{'class':'btn btn-primary'})
#        for link in image_links:
#            image = link["href"] 
#            path_and_name =  os.path.split(image)
#            image_name = path_and_name[1]
#            if image_name[:-4] != '.jpg':
#                image_name += '.jpg'
#            if not os.path.exists(directory + image_name):    
#                r2 = requests.get(image)
#            
#                with open(directory + image_name, "wb") as f:
#                        f.write(r2.content)
#        print("Completed: " + url)
    else:
        r = requests.get(url)
        
        #directory = os.getcwd() + "\\" + url_split[3] +"\\"+ url_split[4]+"\\"
        html_file = "G:\\My Drive\\" +"\\" + url_split[3] +"\\"+ url_split[4]+"\\"+url_split[4]+".html"
        if not os.path.exists(html_file):
            with open(html_file, "w") as f_html:
                        f_html.write(r.text)
            print("Wrote " + url_split[4]+".html" )
        else:
              
            print("Skipped: " +url)

def image_url_gathering():
    html_files = glob.glob("G:\\My Drive\\report\\*\\*.html")
    
    count = 11262
    for file in html_files[11262:]:
        fp = file.split('\\')
        directory = "G:\\My Drive" +"\\" + fp[2] +"\\"+ fp[3]+"\\"
        with open(file, "r") as f_html:
            html = f_html.read()
        soup = bs(html,'lxml')
        
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
                print("Completed: " + image_name + " Count: "+str(count))
            else:
                print("Skipped: " + image_name + " Count: "+str(count))
        count += 1


#df = pd.read_csv('cleaned_tick_data.csv', encoding='utf-8')
#count = 0
##df_state = df["State"] == "AL"
#
#for url in df['URL']:#df[df_state]["URL"]:
#    #print(url)
#    html_request(url)#'https://www.tickreport.com/report/55483')#'https://www.tickreport.com/report/6251')
#    count += 1
#
#print("Completed: " + str(count) + " Image Downloads")