# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:19:02 2018

@author: aubrooks
"""

from glob import glob
from bs4 import BeautifulSoup as bs
import pandas as pd


def get_species_data(root_file_path=''):
    html_files = glob(root_file_path + 'report\\*\\*.html') #"G:\\My Drive\\" +
    list_of_dicts = []
    
    
    for html_fname in html_files:
        ID = html_fname.split('\\')[-1].split('.')[0]
        
        with open(html_fname, "r") as f:
            html = f.read()
        
        soup = bs(html, 'lxml')
        paragraph = soup.p
        print(paragraph)
        print(html_fname)
        if paragraph:
            while paragraph.strong:
                paragraph.strong.unwrap()
            print(paragraph)
            dat_list = []
            for s in paragraph.stripped_strings:
                print(s)
                dat_list.append(s)
                if s == "Other (tick)":
                    dat_list.append("")
                
            print(dat_list)
            dict_row = {"ID":ID,"Species":dat_list[1],"Common Name":dat_list[2],"Sex":dat_list[4],"Stage":dat_list[6],"Feeding State":dat_list[8]}
            list_of_dicts.append(dict_row)
    
    df = pd.DataFrame(list_of_dicts)
    return df


df = get_species_data("G:\\My Drive\\")
df.to_csv('tick_species_data.csv', encoding='utf-8')