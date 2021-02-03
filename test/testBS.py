# -*- codeing = utf-8 -*-
# @Time :2021/1/19 10:06
# @Author: Kas Huang
# @File:testBS.py
# @Software:PyCharm

from bs4 import BeautifulSoup

'''
這裡使用 encoding="utf-8" 否則BS報錯 BeautifulSoup 報錯UnicodeDecodeError
'''
listhtml = open("../page.html", "r", encoding="utf-8")
bs = BeautifulSoup(listhtml, "html.parser")

result_link = bs.select(".list .e.e3")  # 選擇器,ID用#,class用.,往下層級用>

for i in result_link:
    # print(i['href'])  # 印出連結
    # print(i.string)  # 只印出TAG裡的字串
    print(i.em.string, i.aside.string, i.span.string, i.i.string, i['href'])  # 地區,取得公司名,職位,薪水,頁面連結



