# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:20:09 2020

@author: ZYC
"""

import csv

with open('2019-12销售数据汇总.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    filenames = ['2019-12-%02d-销售数据.csv' % (i + 1) for i in range(5)]
    for filename in filenames:
        with open(filename, newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            if filename == filenames[0]:
                rows = csv_reader
            else:
                rows = list(csv_reader)[1:]
            csv_writer.writerows(rows)
    
with open('2019-12销售数据统计汇总表.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    with open('2019-12销售数据汇总.csv', newline='') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            if index == 0:
                csv_writer.writerow(row + ['购买转化率', '客单价'])
            else:
                visitors = int(row[2])  # 访客数
                buyers = int(row[3])  # 买家数
                gmv = int(row[4])  # 交易额
                sale_rate = buyers / visitors if visitors else 0  # 购买转化率
                pct = gmv / buyers if buyers else 0  # 客单价
                csv_writer.writerow(row + [sale_rate, pct])
            