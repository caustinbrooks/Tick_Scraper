# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:35:42 2018

@author: caustinbrooks
"""

#from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from get_dates import get_all_days
#from pprint import pprint



#df_list = []

#states = []






#start_dates, end_dates = get_dates(2006,2018)

#tick_count_by_state = {}
#tick_count_by_state = {'AL': 81, 'AK':0, 'AZ': 5, 'AR': 64, 'CA': 1313,
#                       'CO': 50, 'CT': 1000, 'DE': 110, 'DC': 32, 'FL': 209,
#                       'GA': 165, 'ID': 13, 'IL': 318, 'IN': 177, 'IA': 63,
#                       'KS': 87, 'KY': 97, 'LA': 18, 'ME': 2643, 'MD': 922,
#                       'MA': 16573, 'MI': 184, 'MN': 249, 'MS': 34, 'MO': 113,
#                       'MT': 29, 'NE': 48, 'NV': 8, 'NH': 2644, 'NJ': 1423,
#                       'NM': 6, 'NY': 4824, 'NC': 451, 'ND': 16, 'OH': 274,
#                       'OK': 79, 'OR': 182, 'PA': 1475, 'RI': 834, 'SC': 67,
#                       'SD': 6, 'TN': 245, 'TX': 89, 'UT': 13, 'VT': 1394,
#                       'VA': 1546, 'WA': 179, 'WV': 81, 'WI': 443, 'WY': 8}


def request_scrape(states=['AL'], tick_count_by_state={}):
    data_dict={}
    for state in states:
        print(state)
        state_request = requests.post(
                        "https://www.tickreport.com/stats/search_results",
                        data = (dict(state=state)))
        state_soup = bs(state_request.text,'lxml')
        
        tick_count_soup =  state_soup.find("h3")
        if tick_count_soup != None:
            tick_count_by_state[state] = int(tick_count_soup.strong.text.replace(',',''))         
            #print(tick_count_soup.strong.text.replace(',',''))
            if tick_count_by_state[state] > 250:
                data_dict[state] = query_by_date(state)
            
            else:
                table = parse_table(state_soup)
                data_dict[state] =  pd.read_html(str(table),header=0)[0]
        
        else:
            tick_count_by_state[state] = 0
    
    return data_dict    


def combine_data_dict(data_dict):
    result = pd.concat([pd.DataFrame(data_dict[key]) for key in data_dict.keys()],ignore_index=True)
    return result

def write_df_to_file(df,fname):
    df.to_csv(fname)


def query_by_date(state):
    
    start_dates = get_all_days(2018,2018)
    end_dates = start_dates[1:]
    df_list = []
    for start, end in zip(start_dates,end_dates):
        print(start,end)
        date_request = requests.post(
                        "https://www.tickreport.com/stats/search_results",
                        data = (dict(state=state,
                                     start_date=start,
                                     end_date=end
                                     )))
        date_soup = bs(date_request.text,'lxml')
        tick_count_soup =  date_soup.find("h3")
        
        #Make sure the request returns more than zero rows 
        if tick_count_soup != None:
           table = parse_table(date_soup)
           df_list.append( pd.read_html(str(table),header=0)[0])
    if len(df_list) > 0:     
        result = pd.concat([pd.DataFrame(df_list[i]) for i in range(len(df_list))],ignore_index=True)
        return result
    else:
        return None
def parse_table(soup=''):
    table_list = soup.findAll("table", {"class": "table table-striped table-hover"})#[0]
        #ptable = table.prettify()
    if table_list != []:
        table = table_list[0]
        for row in table.tbody.children:
            #print(row)
            if row != "\n" and row != None:
                for td_tup in enumerate(row.children):
                    if td_tup[1] != '\n' and td_tup[1] != None and td_tup[1].a != None:
                        #print(td_tup)
                        if td_tup[1].a != None  and td_tup[1].a.has_attr('class') != True:
                            td_tup[1].a["href"]
                            td_tup[1].a.string = td_tup[1].a["href"]
                        if td_tup[1].a.has_attr('class'):
                            for test_label in td_tup[1].children:
                                if test_label != '\n':
                                    #print(test_label)
                                    new_tag = soup.new_tag('td')
                                    new_tag.string = test_label['title'] #use this for requests
                                    #new_tag.string = test_label['data-original-title'] #use this for selenium
                                    test_label.replace_with(new_tag)
                                    #test_label.string = test_label["data-original-title"]
                                    #print(test_label)
                    #print(str(row)[1])
        return table
        
        #for row in enumerate(table.tbody.tr.next_siblings):
            

#def selenium_scrape(states = [],tick_count_by_state = {}):
#    df_list = []
#    driver = webdriver.Chrome()
#    driver.get("https://www.tickreport.com/stats")
#    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()
#    #element = driver.find_element_by_name("state")
#    #all_options = element.find_elements_by_tag_name("option")
#    #for option in all_options:
#    #    if option.get_attribute("value") != '':
#    #        states.append(option.get_attribute("value"))
#    
#    for state in states:
#    
#        driver.find_element_by_name("state").click()
#        Select(driver.find_element_by_name("state")).select_by_value(state)
#        driver.find_element_by_name("state").click()
#        driver.find_element_by_xpath("//input[@value='Search'][@type='submit']").click()
#        
#        soup = bs(driver.page_source,'lxml')
#        
#        tick_count_soup =  soup.find("h3")
#        if tick_count_soup != None:
#            tick_count_by_state[state] = int(tick_count_soup.strong.text.replace(',',''))
#        else:
#            tick_count_by_state[state] = 0
#        table = parse_table(soup)
##        table_list = soup.findAll("table", {"class": "table table-striped table-hover"})#[0]
##        #ptable = table.prettify()
##        if table_list != []:
##            table = table_list[0]
##            for row in table.tbody.children:
##                if row != "\n" and row != None:
##                    for td_tup in enumerate(row.children):
##                        if td_tup[1] != '\n' and td_tup[1] != None and td_tup[1].a != None:
##                            #print(td_tup)
##                            if td_tup[1].a != None  and td_tup[1].a.has_attr('class') != True:
##                                td_tup[1].a["href"]
##                                td_tup[1].a.string = td_tup[1].a["href"]
##                            if td_tup[1].a.has_attr('class'):
##                                for test_label in td_tup[1].children:
##                                    if test_label != '\n':
##                                        #print(test_label)
##                                        new_tag = soup.new_tag('td')
##                                        new_tag.string = test_label['data-original-title']
##                                        test_label.replace_with(new_tag)
##                                        #test_label.string = test_label["data-original-title"]
##                                        #print(test_label)
##                        #print(str(row)[1])
##            
##            
##            #for row in enumerate(table.tbody.tr.next_siblings):
#        df_list.append( pd.read_html(str(table),header=0)[0])
#            
#    #print(tick_count_by_state)        
#    result = pd.concat([pd.DataFrame(df_list[i]) for i in range(len(df_list))],ignore_index=True)
#    #pprint(str(table))
#    #pprint(table)
#    #pprint(soup)
#    
#    
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Disease'])[1]/following::input[1]").click()
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Test Results'])[1]/following::i[1]").click()
#    ## ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Feeding State:'])[1]/following::img[1]").click()
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Feeding State:'])[1]/following::div[4]").click()
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='View Original'])[1]/following::img[1]").click()
#    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='View Original'])[1]/following::button[1]").click()
#    #
#    driver.quit()
#    return result


states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
          'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
          'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    
data_dict = request_scrape(states)
df = combine_data_dict(data_dict)
df.to_csv("raw_tick_data.csv")