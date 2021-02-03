# coding=gbk
# @Time :2021/2/1 10:06
# @Author: Kas Huang
# @File:test2dba.py
# @Software:PyCharm

import sqlite3


def main():
    dbpath = "job_result.db"
    datalist = [{'link': 'https://msearch.51job.com/jobs/zhongshan/126844239.html?rc=03', 'location': '中山', 'company': '中山东菱威力电器有限公司', 'job': '外贸区域经理（滚筒洗衣机）', 'salary': '7.5-8千/月'}, {'link': 'https://msearch.51job.com/jobs/sanya/125695713.html?rc=03', 'location': '三亚', 'company': '海南亚特兰蒂斯商旅发展有限公司亚特兰蒂斯酒店', 'job': '洗衣房技工', 'salary': '3-4.5千/月'}, {'link': 'https://msearch.51job.com/jobs/nanjing/124087797.html?rc=03', 'location': '南京-建邺区', 'company': '新寰亚（上海）健康管理有限公司', 'job': '洗衣工', 'salary': '3-4.5千/月'}, {'link': 'https://msearch.51job.com/jobs/harbin/128510697.html?rc=03', 'location': '哈尔滨', 'company': '哈尔滨鸿派人力资源服务有限公司', 'job': '洗衣工', 'salary': '2.5-4千/月'}, {'link': 'https://msearch.51job.com/jobs/guangzhou/126037018.html?rc=03', 'location': '广州-海珠区', 'company': '保利商业- 比邻洗衣事业部', 'job': '洗衣技术主管', 'salary': '6-8千/月'}, {'link': 'https://msearch.51job.com/jobs/jinhua/127577489.html?rc=03', 'location': '异地招聘', 'company': '杭州川洋贸易有限公司', 'job': '金华区域销售主管（美的冰箱、美的洗衣机）', 'salary': '15-20万/年'}, {'link': 'https://msearch.51job.com/jobs/wuhan/128466886.html?rc=03', 'location': '武汉-洪山区', 'company': '武汉生物城文化旅游投资开发有限公司光谷皇冠假日酒店分公司', 'job': '洗衣房经理', 'salary': '6-8千/月'}, {'link': 'https://msearch.51job.com/jobs/changsha/114977380.html?rc=03', 'location': '长沙-雨花区', 'company': '长沙皮斯托皮具护理有限公司', 'job': '洗衣师助理', 'salary': '3.5-5千/月'}]

    for data in datalist:
        print(data['link'], data['location'], data['company'], data['job'], data['salary'])

    save_2db(datalist, dbpath)


def save_2db(datalist, dbpath):  # 保存数据 以DATABASE方式
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    # 執行SQL語句X次,寫入每个工作5个資料
    # 去除特殊符號 str.replace("/r","") 替換"/r"為空白
    # 字符串截取: str.[n:m] 截取从下标n到m个字符
    # 語法 info = days[0]["title"].split("|")   # 去除前后空格 str.strip()

    for data in datalist:
        # sql = '''insert into job (detail_link,location,company,job,salary) values ('%s','%s','%s','%s','%s')''' % (
        # data['link'], data['location'], data['company'], data['job'], data['salary'])
        # 3.5-5千/月 , 15-20万/年 , 7.5-8千/月 , 3-4.5千/月
        a = data['salary']
        if "万/年" in data['salary']:
            # continue
            a = a.replace("万/年", "")
            a = a[a.find("-") + 1:]
            a = float(a) * 10 / 12

        else:
            a = a.replace("千/月", "")
            a = a[a.find("-") + 1:]
        b = float(a) * 1000

        sql = '''insert into job (detail_link,location,company,job,salary) 
        values ('%s','%s','%s','%s','%s')''' % (data['link'], data['location'], data['company'], data['job'], b)

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):  # 創建數據庫
    sql = '''
        create table job
        (
        id integer primary key autoincrement,
        detail_link text,
        location text,
        company text,
        job text ,
        salary varchar 
        )
        '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
    print("test over")
