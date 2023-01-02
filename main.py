#!/usr/bin/env python3
import datetime
import os
# from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import glob
import sys 
import re
import csv

dirname = 'log_files/*.log'

years = ['2020','2021','2022','2023']

months = ['1','2','3','4','5','6','7','8','9','10','11','12']

test = 2022

# for file in os.listdir(dirname):
#     if file.endswith(ext):
#         with open(file):

cnt = 0

def filter_year(c_year,row):
    global yearly
    global cnt
    date = datetime.datetime.strptime(str(row[0]), '%d/%m/%y')
    # date = datetime.datetime.strftime(date, '%d/%m/%y')
    if date.year == c_year:
        yearly.append(row)
        cnt = cnt + 1
            
files= glob.glob(dirname)

data = []
yearly = []

count = 0

for filename in files:
       
    with open(filename, 'r', encoding='latin-1') as file:
    
        while (line := file.readline().rstrip()):
            line = re.split(r'\s+', line)
            
            if len(line) > 5:
                if len(line[0]) == 10:
                    # print('IN')
                    count = count +1
                    date = datetime.datetime.strptime(str(line[0]), '%d/%m/%Y')
                    line[0] = datetime.datetime.strftime(date, '%d/%m/%y')
                    row = [line[0], line[1]]
                    data.append(row)
                    filter_year(test,row)
                else:
                    # print('OUT')
                    count = count +1
                    row = [line[0], line[1]]
                    data.append(row)
                    filter_year(test,row)
                
                
                
with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    # print(data)                  

print(yearly)
print(count)
print(cnt)



            # for word in re.split(r'\s+', line):
            #     print(line)
    
    
    
    # with open(file, 'r', encoding="UTF-8") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         for word in line.split('\n'):
    #             if word in line.split(':')== 'Engecard n�o respondendo':
    #                 print(line)