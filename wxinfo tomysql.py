# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:06:59 2017

@author: vigh
"""
import itchat
import requests
import csv
import pymysql.cursors
itchat.login()
friends = itchat.get_friends(update=True)[0:]


 
for i in friends:
    city=i['City']
    province=i['Province']
    signature=i['Signature']
    nickname=i['NickName']
    sex=i['Sex']
    
#获取数据库链接  
    connection=pymysql.connect(host='localhost',
                           user='root',
                           password='1234',
                           db='wx',
                           charset='utf8mb4')
    try:
    #获取会话指针
        with connection.cursor() as cursor:
            sql="insert into `friendinfo`(`province`,`city`,`sex`) values(%s,%s,%s) "
            cursor.execute(sql,(
                                province,
                                city,
                                sex,
                                )
                                ) 
        connection.commit()
    finally:
        connection.close()
