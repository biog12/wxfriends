import itchat
import re

itchat.login()#登录
friends = itchat.get_friends(update=True)[0:]#get 好友信息
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)

# 拼接字符串
text = "".join(tList)

# jieba分词
import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image

# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000, 
                         max_font_size=40, random_state=42,
                         font_path='C:\Windows\Fonts\simhei.ttf').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.savefig("签名",dpi=1024)
plt.show()
