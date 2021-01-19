# -*- codeing = utf-8 -*-
# @Time :2021/1/19 10:06
# @Author: Kas Huang
# @File:testBS.py
# @Software:PyCharm


from bs4 import BeautifulSoup
'''
這裡使用 encoding="utf-8" 否則BS報錯 BeautifulSoup 報錯UnicodeDecodeError
'''
listhtml = open("page.html", "r", encoding="utf-8")
bs = BeautifulSoup(listhtml, "html.parser")

resultList = bs.select(".list .e.e3")  # 選擇器,ID用#,class用.,往下層級用>

for i in resultList:
    print(i["href"])  # 這可能是BS4的語法

