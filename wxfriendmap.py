# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:00:08 2017

@author: vigh

"""
#获取城市列表loc,频率列表locp
import itchat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
itchat.login() #微信登录
#获取好友列表
friends = itchat.get_friends(update=True)[0:]
i=0
a=[]#好友城市列表
for i in range(len(friends)):
    a.append(friends[i].City)
    i+=1
loc=[]
loc=list(set(a))#好友城市不重复列表
for index, value in enumerate(loc):
    if value=='':
       loc[index]='未知'
#城市不重复集合出现的次数统计
b=set(a)#城市不重复集合
locp=[]#城市频率
for item in b:
     locp.append(a.count(item))





#baidu mapapi获取城市的经纬度   
import requests 
import json
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/' #bidumap url
    output = 'json'
    ak = 'wFdfBljwyuqKCZviBfpiPRwI786RTC2K' #密钥
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = requests.get(uri) #requests 包 get url
    temp = json.loads(temp.text)
    return temp
#城市列表经纬度
i=0
d=dict() #get data 保存字典
for i in range(len(loc)):
        d[i]=getlnglat(loc[i])
        #print(loc[i],d[i]['result']['location']['lng'],d[i]['result']['location']['lat'])





## map
import time

start = time.clock()

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
plt.rcParams['font.sans-serif']=['SimHei']
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

map = Basemap(llcrnrlon=80.33, 
              llcrnrlat=3.01, 
              urcrnrlon=138.16, 
              urcrnrlat=56.123,
             resolution='h', projection='cass', lat_0 = 42.5,lon_0=120,ax=ax1)

shp_info = map.readshapefile("C:\\Users\\vigh\\Downloads\\CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域

#for info, shp in zip(map.states_info, map.states):
#    proid = info['NAME_1']  # 可以用notepad打开CHN_adm1.csv文件，可以知道'NAME_1'代表各省的名称
#    if proid == 'Guangdong':
#        poly = Polygon(shp,facecolor='g',edgecolor='c', lw=3) # 绘制广东省区域
#        ax1.add_patch(poly)
#
map.shadedrelief() # 绘制阴暗的浮雕图

map.drawcoastlines()

#绘制城市对应的点
for i in range(len(loc)):
        x,y = map(d[i]['result']['location']['lng'], d[i]['result']['location']['lat'])
        map.plot(x, y, marker=',',color='r')
        plt.scatter(x,y,s=locp[i]/len(a)*50)
        plt.text(x,y,loc[i],color='b',fontsize=2,ha='left',va='baseline')

end=time.clock()
print(end-start)
plt.savefig('map',dpi=900)
plt.show()
