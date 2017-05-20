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
#
b=set(a)#城市不重复集合
#城市不重复集合出现的次数统计
d=[]
for item in b:
     d.append(a.count(item))
#柱状图
plt.bar(range(len(d)),d,tick_label=c,width=0.5,align="center")
plt.xticks(rotation=90)
plt.title("好友地理位置统计")
plt.savefig('dili',dpi=800)
plt.show()
