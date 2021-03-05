# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:00:42 2021

@author: liucaixiong
"""

import pandas as pd
import numpy as np
from random import shuffle
from datetime import datetime

import time
import re
import os




def listdir(path):
    file_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        file_list.append(file_path)
      
    return file_list


def datetime_to_stamp(datetime_str):

    now = time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    
    timestamp = time.mktime(now)
    
    return timestamp


def stamp_to_datetime(timestamp):
    
    x = time.localtime(timestamp)
    
    date_time = time.strftime('%Y-%m-%d %H:%M:%S',x)
    
    return  date_time





def get_offline_days(offline): # 离线天数，如果是na值，就返回0

    if len(str(offline)) >= 5:
        timelist = regex.split(offline)
        offline_time = int(timelist[0]) + int(timelist[1])/24 + int(timelist[2])/1440
        if offline_time > 0  and offline_time < 1 :
            return 1
        else:
            return int(np.floor(offline_time))
    else:
        return 0
     
    
def get_offline_days_na(offline): # 离线天数，如果是na值，依旧返回na值

    if len(str(offline)) >= 5:
        timelist = regex.split(offline)
        offline_time = int(timelist[0]) + int(timelist[1])/24 + int(timelist[2])/1440
        if offline_time > 0  and offline_time < 1 :
            return 1
        else:
            return int(np.floor(offline_time))


def get_days(date_time):   # 报警的天数
    
    if len(str(date_time)) < 5:
        return 0
    else:
        #today = '2020-08-21'
        today = datetime.now().strftime('%Y-%m-%d')
        date_time1 = str(date_time)[0:10]
        delta = datetime.strptime(today,'%Y-%m-%d') - datetime.strptime(date_time1,'%Y-%m-%d')
        return delta.days + 1




def get_offline_hours(offline): #离线的小时数
    
    if len(str(offline)) >= 5:
        timelist = regex.split(offline)
        offline_time = int(timelist[0])*24 + int(timelist[1]) + int(timelist[2])/60
        return round(offline_time,2)
    else:
        return 0


def get_alarm_hours(date_time): # 报警的小时数
    if date_time == 0:
        return 0
    else:
        delta = datetime.now() - datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
        hours = delta.days * 24 + delta.seconds/3600
        return round(hours,2)
    

def transform_string(x):
    if x == 0:
        return ''
    else:
        return str(int(x))
            
    
def get_percent_power(val):
    if val == 0:
        return ''
    else:
        return str(int(100*val)) + '%'
    

def get_power(val):
    if val == 0:
        return 0
    else:
        return int(val[:-1])        



with open(r'C:\Users\liucaixiong\Desktop\SQL工作空间\columns.txt', mode = 'r', encoding = 'utf-8') as file:
    items=[]
    for line in file.readlines():
        item = line.strip()
        items.append(item)
    
  






