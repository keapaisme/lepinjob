# -*- codeing = utf-8 -*-
# @Time :2021/1/18 13:26
# @Author: Kas Huang
# @File:spiderLK.py
# @Software:PyCharm

from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import urllib.error
import sqlite3

# baseurl = "https://www.liepin.com/zhaopin/?init=-1&fromSearchBtn=2&degradeFlag=0&key=" + parse.quote(keytitle) + "&d_sfrom=search_unknown&d_pageSize=40&curPage=%d"%pageNum  # 猎聘
# keytitle = input("請輸入要搜尋的工作 :")
# keycity = input("請輸入要搜尋的地區 :") 340000澳門,090200成都,010000北京,040000深圳,000000所有
keycity = "000000"
keyTitle = "洗"  # 測試用,正常使用時改以上方方式輸入
job_keyword = "经理"
# pageNum = 0  # 51job 要用1, 猎聘用0
kw = parse.quote(parse.quote(keyTitle))  # 原網站將中文編譯兩次所以出現%25字節

job_data = {}  # 每个记录是一个列表,每个列表中有多个键值对
# {"link":"http://www.123.com","cname":"xxx","jname":"pythoxx","salary":"2000/月"}

job_list = []  # 所有的工作岗位信息,放到列表中,每个列表的元素是上面的字典
# [{},{},{}]


def main():
    for i in range(1, 51):
        # url = "https://search.51job.com/list/000000,000000,0000,00,9,99," + kw + ",2," + str(i) + ".html"  # 不準
        url = "https://msearch.51job.com/job_list.php?keyword="+kw+"&keywordtype=2&jobarea="+keycity+"&fromapp=&pageno="+str(i)+""
        # 猎聘不能用 url = "https://www.liepin.com/zhaopin/?init=-1&fromSearchBtn=2&degradeFlag=0&key=" + parse.quote(keyTitle) + "&d_sfrom=search_unknown&d_pageSize=40&curPage="+str(i-1)+""  # 猎聘
        # print(url) 印出各頁連結
        page_number = get_data(url)
        if len(page_number) == 0:
            break
    dbpath = "job_result.db"
    save_data_2db(job_list, dbpath)


def ask_url(url):
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


def get_data(url):
    html = ask_url(url)
    # 逐一解析數据
    bs = BeautifulSoup(html, "html.parser")
    result_link = bs.select(".list .e.e3")  # 選擇器,ID用#,class用.,往下層級用>
    x = 0
    for n in result_link:
        #  print(x, i.em.string, i.aside.string, i.span.string, i.i.string, i['href'])  # 地區,取得公司名,職位,薪水,頁面連結
        #  datalist.append(i['href'])  # 將該頁面取得的link放入datalist[]中
        if job_keyword in n.span.string:  # 若職位有"洗"才放進字典
            job_list.append({"link": n['href'], "location": n.em.string, "company": n.aside.string, "job": n.span.string, "salary": n.i.string})
        #   print(job_list, end="\n")  # 列出符合篩選的工作列表
        #   print(job_list[x-1]['job'], job_list[x-1]['salary'])  # 印出己經篩選過職位JOB有包括job_keyword的職位名稱
        #   print(n.em.string, n.aside.string, n.span.string, n.i.string)
        else:
            pass
    return result_link


def save_data_2db(detail, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    # 執行SQL語句X次,寫入每个工作5个資料
    # 去除特殊符號 str.replace("/r","") 替換"/r"為空白
    # 字符串截取: str.[n:m] 截取从下标n到m个字符
    # 語法 info = days[0]["title"].split("|")   # 去除前后空格 str.strip()

    for data in job_list:
        # sql = '''insert into job (detail_link,location,company,job,salary) values ('%s','%s','%s','%s','%s')''' % (
        # data['link'], data['location'], data['company'], data['job'], data['salary'])
        # 3.5-5千/月 , 15-20万/年 , 7.5-8千/月 , 3-4.5千/月
        a = data['salary']
        '''若原始薪資資料無填寫,data['salary']會為None,所以將其轉成字串格式0元'''
        # print(type(a))

        if str(a) == 'None':
            a = "-0千/月"
            b = 0
        if "千以" in a:
            a = "-0千/月"
            b = 0
        b = 1
        if "万/年" in a:
            b = 0.83333333
        elif "万/月" in a:
            b = 10

        a = a[a.find("-") + 1:a.find('/') - 1]
        salary = float(a) * b * 1000

        # print(salary)

        sql = '''insert into job (detail_link,location,company,job,salary) 
            values ('%s','%s','%s','%s','%s')''' % (data['link'], data['location'], data['company'], data['job'], salary)

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
            create table if not exists job
            (
            id integer primary key autoincrement,
            detail_link text,
            location text,
            company text,
            job text ,
            salary numeric 
            )
            '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
    print("爬取 over", end='\n')
    print('%s地區共有%d筆符合查詢' % (keycity, len(job_list)))
    print(job_list)

