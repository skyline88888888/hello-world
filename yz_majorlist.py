#yz_majorlist.py
import requests
from bs4 import BeautifulSoup
import numpy as np
def getHtmlText(url):
    try:
        res=requests.get(url)
        res.raise_for_status()
    except:
        print("html文本获取异常")
    return res.text
keys=np.arange(100801,100840,1)
keys=list(keys)
for i in range(100870,100873,1):
    keys.append(i)
urls=[]
for k in keys:
    options={"method":"subCategoryXk","key":str(k)}
    response=requests.post("https://yz.chsi.com.cn/zyk/specialityCategory.do",data=options)
    soup=BeautifulSoup(response.text,"html.parser")
    tabelement=soup.find("table")
    elements=tabelement.find_all("tr")
    for e in elements[1:]:
        newelements=e.find("a")
        urls.append("https://yz.chsi.com.cn"+newelements.attrs["href"])
writestr=""
for u in urls:
    try:
        html=getHtmlText(u)
        soup=BeautifulSoup(html,"html.parser")
        title=soup.find("div",attrs={"class","container zyk-detail clearfix"}).find("h2").text
        universities=""
        for e in soup.find("ul",attrs={"class","clearfix"}).findAll("li"):
            universities=universities+e["title"]+"/"
        writestr=writestr+title+","+universities+"\n"
    except:
        print(u)
with open("yz.csv","w") as f:
    f.write(writestr)
f.close()
    
    

