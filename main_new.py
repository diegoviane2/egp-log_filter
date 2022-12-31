#!/usr/bin/env python3

import datetime
import glob

# main_path = 'log_files/*.log'

# def filter_files(path):
#     files = glob.glob(path)
#     for file in files:
#         with open(file, 'r') as f
#             while(line := f.readline().rstrip()):
#                 line = re.split(r's\+', line)
#                 if len(line) > 5;
                
                
date1 = '26/12/1990'

print(date1)

date2 = datetime.datetime.strptime(date1, '%d/%m/%Y')
date2 = datetime.datetime.strftime(date2, '%d/%m/%y')

print(date2)