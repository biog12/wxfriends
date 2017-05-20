import itchat #itchat包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
itchat.login()
#获取好友列表
friends = itchat.get_friends(update=True)[0:]
i=0
a=[]
for i in range(len(friends)):
    a.append(friends[i].City)
    i+=1
b=set(a)
print(len(friends))
c=[]
d=[]

for item in b:
     c.append(item)
     d.append(a.count(item))

#print(c)
#print(c)
#print(d)
plt.bar(range(len(d)),d,tick_label=c,width=0.5,align="center")
plt.xticks(rotation=90)
plt.title("好友地理位置统计")
plt.savefig('dili',dpi=800)
plt.show()
