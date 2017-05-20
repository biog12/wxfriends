import itchat
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 先登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0
# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 总数算上，好计算比例啊～
total = len(friends[1:])

a=float(male) / total * 100
b=float(female) / total * 100
c=float(other) / total * 100     
# 好了，打印结果
print(u"男性好友：%.2f%%" % (float(male) / total * 100))
print (u"女性好友：%.2f%%" % (float(female) / total * 100))
print (u"其他：%.2f%%" % (float(other) / total * 100))
#pie chart
labels = u'男性好友', u'女性好友',u'其他'
sizes = [a,b,c]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title(u'微信好友统计')
plt.savefig("999",dpi=600)

