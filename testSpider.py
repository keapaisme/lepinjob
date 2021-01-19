
import urllib.request
from urllib import parse
import urllib.error



# keytitle = input("請輸入要搜尋的工作 :")
# keycity = input("請輸入要搜尋的地區 :") 090200成都,010000北京,040000深圳,000000所有
keytitle = "洗衣" # 測試用,正常使用時改以上方方式輸入
pageNum = 1
kw = parse.quote(parse.quote(keytitle))  # 原網站將中文編譯兩次所以出現%25字節



def main():

    baseurl = "https://search.51job.com/list/000000,000000,0000,00,9,99," + kw + ",2," + str(pageNum) + ".html"
    # baseurl = "https://www.liepin.com/zhaopin/?init=-1&fromSearchBtn=2&degradeFlag=0&key=" + parse.quote(keytitle) + "&d_sfrom=search_unknown&d_pageSize=40&curPage=%d"%pageNum  # 猎聘
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
        # print(url)  # 測試有否正常捉取網頁
        html = askURL(url)
        print(html)


    return datalist



if __name__=="__main__":
    main()
    print("爬取 over")