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
keytitle = "洗衣"  # 測試用,正常使用時改以上方方式輸入
pageNum = 1  # 51job 要用1, 猎聘用0
kw = parse.quote(parse.quote(keytitle))  # 原網站將中文編譯兩次所以出現%25字節


def main():
    url = "https://search.51job.com/list/090200,000000,0000,00,9,99,"+ kw +",2,"+ str(pageNum) +".html"
    # baseurl = "https://www.liepin.com/zhaopin/?init=-1&fromSearchBtn=2&degradeFlag=0&key=" + parse.quote(keytitle) + "&d_sfrom=search_unknown&d_pageSize=40&curPage=%d"%pageNum  # 猎聘
    getData(url)


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


def getData(url):
    datalist = []
    html = askURL(url)

    # 逐一解析數据
    bs = BeautifulSoup(html, "html.parser")
    result_link = bs.select(".list .e.e3")  # 選擇器,ID用#,class用.,往下層級用>
    x = 0
    for i in result_link:
        x += 1
        # print(i['href'])  # 印出連結
        # print(i.string)  # 只印出TAG裡的字串
        # strlist = i.em.string + i.aside.string + i.span.string + i.i.string + i['href']
        print(x, i.em.string, i.aside.string, i.span.string, i.i.string, i['href'])  # 地區,取得公司名,職位,薪水,頁面連結

    return datalist


def saveData2DB(detail, dbpath):
    pass


def init_db(dbpath):
    pass


if __name__ == "__main__":
    main()
    print("爬取 over")