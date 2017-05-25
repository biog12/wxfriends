# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:06:59 2017

@author: vigh
"""
import itchat
import requests
import csv
itchat.login()
friends = itchat.get_friends(update=True)[0:]

#将数据写入csv文件
csvfile = open('friend2.csv', 'w', newline='')  # , encoding='utf-8'  
writer = csv.writer(csvfile)  
writer.writerow(['nickname', 'province','city', 'sex',  'signature', ])  
for i in friends:
    city=i['City']
    province=i['Province']
    signature=i['Signature']
    nickname=i['NickName']
    sex=i['Sex']
    #去除非字符编码
    writer.writerow([nickname.encode('gbk', 'ignore').decode('gbk'),
                     province,
                     city,
                     sex,
                     signature.encode('gbk', 'ignore').decode('gbk')])
csvfile.close()   
