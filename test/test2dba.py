# coding=gbk
# @Time :2021/2/1 10:06
# @Author: Kas Huang
# @File:test2dba.py
# @Software:PyCharm

import sqlite3


def main():
    dbpath = "job_result.db"
    datalist = [{'link': 'https://msearch.51job.com/jobs/zhongshan/126844239.html?rc=03', 'location': '��ɽ', 'company': '��ɽ���������������޹�˾', 'job': '��ó��������Ͳϴ�»���', 'salary': '7.5-8ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/sanya/125695713.html?rc=03', 'location': '����', 'company': '������������˹���÷�չ���޹�˾��������˹�Ƶ�', 'job': 'ϴ�·�����', 'salary': '3-4.5ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/nanjing/124087797.html?rc=03', 'location': '�Ͼ�-������', 'company': '����ǣ��Ϻ��������������޹�˾', 'job': 'ϴ�¹�', 'salary': '3-4.5ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/harbin/128510697.html?rc=03', 'location': '������', 'company': '����������������Դ�������޹�˾', 'job': 'ϴ�¹�', 'salary': '2.5-4ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/guangzhou/126037018.html?rc=03', 'location': '����-������', 'company': '������ҵ- ����ϴ����ҵ��', 'job': 'ϴ�¼�������', 'salary': '6-8ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/jinhua/127577489.html?rc=03', 'location': '�����Ƹ', 'company': '���ݴ���ó�����޹�˾', 'job': '�������������ܣ����ı��䡢����ϴ�»���', 'salary': '15-20��/��'}, {'link': 'https://msearch.51job.com/jobs/wuhan/128466886.html?rc=03', 'location': '�人-��ɽ��', 'company': '�人������Ļ�����Ͷ�ʿ������޹�˾��Ȼʹڼ��վƵ�ֹ�˾', 'job': 'ϴ�·�����', 'salary': '6-8ǧ/��'}, {'link': 'https://msearch.51job.com/jobs/changsha/114977380.html?rc=03', 'location': '��ɳ-�껨��', 'company': '��ɳƤ˹��Ƥ�߻������޹�˾', 'job': 'ϴ��ʦ����', 'salary': '3.5-5ǧ/��'}]

    for data in datalist:
        print(data['link'], data['location'], data['company'], data['job'], data['salary'])

    save_2db(datalist, dbpath)


def save_2db(datalist, dbpath):  # �������� ��DATABASE��ʽ
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    # ����SQL�Z��X��,����ÿ������5���Y��
    # ȥ�������̖ str.replace("/r","") ��Q"/r"��հ�
    # �ַ�����ȡ: str.[n:m] ��ȡ���±�n��m���ַ�
    # �Z�� info = days[0]["title"].split("|")   # ȥ��ǰ��ո� str.strip()

    for data in datalist:
        # sql = '''insert into job (detail_link,location,company,job,salary) values ('%s','%s','%s','%s','%s')''' % (
        # data['link'], data['location'], data['company'], data['job'], data['salary'])
        # 3.5-5ǧ/�� , 15-20��/�� , 7.5-8ǧ/�� , 3-4.5ǧ/��
        a = data['salary']
        if "��/��" in data['salary']:
            # continue
            a = a.replace("��/��", "")
            a = a[a.find("-") + 1:]
            a = float(a) * 10 / 12

        else:
            a = a.replace("ǧ/��", "")
            a = a[a.find("-") + 1:]
        b = float(a) * 1000

        sql = '''insert into job (detail_link,location,company,job,salary) 
        values ('%s','%s','%s','%s','%s')''' % (data['link'], data['location'], data['company'], data['job'], b)

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):  # ����������
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
