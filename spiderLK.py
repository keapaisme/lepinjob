# -*- codeing = utf-8 -*-
# @Time :2021/1/18 13:26
# @Author: Kas Huang
# @File:spiderLK.py
# @Software:PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request
from urllib import parse
import urllib.error
import sqlite3


# keytitle = input("請輸入要搜尋的工作 :")
# keycity = input("請輸入要搜尋的地區 :") 090200成都,010000北京,040000深圳,000000所有
keytitle = "python"
kw = parse.quote(parse.quote(keytitle))  # 原網站將中文編譯兩次所以出現%25字節
pageNum = 0

def main():
    # baseurl = "https://search.51job.com/list/090200,000000,0000,00,9,99," + kw + ",2," + str(pageNum) + ".html"
    baseurl = "https://www.liepin.com/zhaopin/?init=-1&fromSearchBtn=2&degradeFlag=0&key=" + parse.quote(keytitle) + "&d_sfrom=search_unknown&d_pageSize=40&curPage=%d"%pageNum  # 猎聘
    datalist = getData(baseurl)






def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl
        print(url)  # 測試有否正常捉取網頁
        # html = askURL(url)

        # 逐一解析數据
        soup = BeautifulSoup(html, "html.parser")
        print(soup)
        for item in soup.find_all('div', class_=r"sojob-item-main clearfix"):
            print(item)

    return datalist


def saveData2DB(detail, dbpath):
    pass


def init_db(dbpath):
    pass






if __name__=="__main__":
    main()
    print("爬取 over")