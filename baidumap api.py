import requests 
import json
#获取地址经纬度函数
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/' #bidumap url
    output = 'json'
    ak = 'wFdfBljwyuqKCZviBfpiPRwI786RTC2K' #密钥
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = requests.get(uri) #requests 包 get url
    temp = json.loads(temp.text)
    return temp

#城市列表
loc=[ '扬州', '惠州', '南通', '烟台', '南昌', 
'滁州', '松原', '黄山', '深圳', '龙岩', '大连',
 '嘉定', '襄阳', '济宁', '长春', '苏州', '海淀', 
 '青岛', '无锡', '蓟县', '南京', '白山', '临汾']
i=0
d=dict() #get data 保存字典
for i in range(len(loc)):
        d[i]=getlnglat(loc[i])
        print(loc[i],d[i]['result']['location']['lng'],
                     d[i]['result']['location']['lat'])
