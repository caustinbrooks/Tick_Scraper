# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:35:42 2018

@author: caustinbrooks
"""

def get_dates(min_year,max_year):      
    years = list(range(min_year,max_year + 1))
    months = list(range(1,13))
    start_dates = []
    end_dates = []
    
    for yyyy in years:
        for mm in months:
            if mm in [1,3,5,7,8,10,12]:
                if mm <10:
                    mm_str = '0'+str(mm)
                else:
                    mm_str = str(mm)
                    
                start_dates.append(str(yyyy)+'-'+mm_str+'-01')
                end_dates.append(str(yyyy)+'-'+mm_str+'-31')
            elif mm in [4,6,9,11]:
                if mm <10:
                    mm_str = '0'+str(mm)
                    
                else:
                    mm_str = str(mm)
                start_dates.append(str(yyyy)+'-'+mm_str+'-01')
                end_dates.append(str(yyyy)+'-'+mm_str+'-30')
            else:
                if mm <10:
                    mm_str = '0'+str(mm)
                    
                else:
                    mm_str = str(mm)
                start_dates.append(str(yyyy)+'-'+mm_str+'-01')
                end_dates.append(str(yyyy)+'-'+mm_str+'-28')
    return start_dates, end_dates

def get_all_days(min_year,max_year):
    years = list(range(min_year,max_year + 1))
    months = list(range(1,13))
    days = list (range(1,32))
    start_dates = []
    
    
    for yyyy in years:
        for mm in months:
            for dd in days:
                
                if mm in [1,3,5,7,8,10,12]:
                    if mm <10:
                        mm_str = '0'+str(mm)
                    else:
                        mm_str = str(mm)
 
                    if dd <10:
                        dd_str = '0' + str(dd)
                    else:
                        dd_str = str(dd)
                        
                    start_dates.append(str(yyyy)+'-'+mm_str+'-'+dd_str)
                    
                elif mm in [4,6,9,11]:
                    if mm <10:
                        mm_str = '0'+str(mm)
                    else:
                        mm_str = str(mm)

                    if dd <10:
                        dd_str = '0' + str(dd)
                    else:
                        dd_str = str(dd)
                    if dd < 31:    
                        start_dates.append(str(yyyy)+'-'+mm_str+'-'+dd_str)
                    
                else:
                    if mm <10:
                        mm_str = '0'+str(mm)           
                    else:
                        mm_str = str(mm)
                    if dd <10:
                        dd_str = '0' + str(dd)
                    else:
                        dd_str = str(dd)
                    if dd < 29:
                        start_dates.append(str(yyyy)+'-'+mm_str+'-'+dd_str)
                    
                    
                    
    return start_dates