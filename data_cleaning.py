# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:46:29 2018

@author: Austin
"""
import pandas as pd


def load_data(fname):
    
    df = pd.read_csv(fname)
   # print (df.head())

    return df

def rename_columns(df):
    df = df.rename(columns={'Unnamed: 0':'ID', '\xa0':'URL',
   'Unnamed: 5':'Borrelia general species', 
   'Unnamed: 6':'Borrelia burgdorferi sensu lato', 
   'Unnamed: 7':'Borrelia miyamotoi', 
   'Unnamed: 8':'Borrelia mayonii', 
   'Unnamed: 9':'Babesia microti',
   'Unnamed: 10':'Ehrlichia muris-Like Agent', 
   'Unnamed: 11':'Anaplasma phagocytophilum', 
   'Unnamed: 12':'Borrelia lonestari', 
   'Unnamed: 13':'Rickettsia rickettsii',
   'Unnamed: 14':'Rickettsia philipii', 
   'Unnamed: 15':'Rickettsia parkeri', 
   'Unnamed: 16':'Francisella tularensis', 
   'Unnamed: 17':'Ehrlichia chaffeensis',
   'Unnamed: 18':'Ehrlichia ewingii', 
   'Unnamed: 19':'Ehrlichia canis', 
   'Unnamed: 20':'Bartonella henselae', 
   'Unnamed: 21':'Babesia duncani',
   'Unnamed: 22':'Babesia divergens', 
   'Unnamed: 23':'Powassan virus general species', 
   'Unnamed: 24':'Powassan virus (type 2, DTV)', 
   'Unnamed: 25':'Heartland virus',
   'Unnamed: 26':'Colorado Tick Fever virus', 
   'Unnamed: 27':'Bourbon virus'})
    
    #print(df.columns)
    return df

def data_cleanup(df):
    
    df = df.drop(['Test Results'],axis=1)
    
    for col in ['Borrelia general species', 'Borrelia burgdorferi sensu lato',
       'Borrelia miyamotoi', 'Borrelia mayonii', 'Babesia microti',
       'Ehrlichia muris-Like Agent', 'Anaplasma phagocytophilum',
       'Borrelia lonestari', 'Rickettsia rickettsii', 'Rickettsia philipii',
       'Rickettsia parkeri', 'Francisella tularensis', 'Ehrlichia chaffeensis',
       'Ehrlichia ewingii', 'Ehrlichia canis', 'Bartonella henselae',
       'Babesia duncani', 'Babesia divergens',
       'Powassan virus general species', 'Powassan virus (type 2, DTV)',
       'Heartland virus', 'Colorado Tick Fever virus', 'Bourbon virus']:
        
        df[col] = df[col].apply(lambda x: x.replace( x, 'N/A' if 'has not been ordered' in x else x.replace(x, 'NEGATIVE' if 'NEGATIVE' in x else 'POSITIVE')))
        df[col] = df[col].apply(lambda x: False if x== 'NEGATIVE' else ( True if x=='POSITIVE' else 'N/A' ))
    
    df['ID'] = df["URL"].str[34:]
    
    return df

fname = "raw_tick_data.csv"
df = load_data(fname)
df = rename_columns(df)
df = data_cleanup(df)
df.to_csv('cleaned_tick_data.csv', encoding='utf-8')











