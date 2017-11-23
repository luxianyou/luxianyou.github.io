#!/usr/bin/python
#-*- coding:utf-8 -*-

from datetime import date
from datetime import timedelta
import random

def getdistrictcode():
    with open('./dirscode.txt','r') as f:
        codelist = f.readlines()
    codelist = [{"code":x.split(',')[0],"city":x.split(',')[1].strip()} for x in codelist if x.strip()]
    return codelist

def gennerator(codelist):
    id = codelist[random.randint(0,len(codelist))]['code'] #地区项
    id = id + str(random.randint(1930,2013)) #年份项
    da  = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项
    id = id + da.strftime('%m%d')
    id = id+ str(random.randint(100,300))#，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id)):
       count = count +int(id[i])*weight[i]
    id = id + checkcode[str(count%11)] #算出校验码
    return id

codelist = getdistrictcode()
id = gennerator(codelist)
print id