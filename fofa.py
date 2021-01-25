import requests
from lxml import etree
import base64
import re
import time
import base
import config
from urllib.parse import quote,unquote

def spider():
    searchbs64 = quote(str(base64.b64encode(config.SearchKEY.encode()), encoding='utf-8'))

    # searchbs64 = (str(base64.b64encode(config.SearchKEY.encode('utf-8')), 'utf-8'))
    print("爬取页面为:https://fofa.so/result?&qbase64=" + searchbs64)
    html = requests.get(url="https://fofa.so/result?&qbase64=" + searchbs64, headers=config.header).text
    pagenum = re.findall('>(\d*)</a> <a class="next_page" rel="next"', html)
    print("该关键字存在页码: "+pagenum[0])
    config.StartPage=input("请输入开始页码:\n")
    config.StopPage=input("请输入终止页码: \n")
    doc = open("hello_world.txt", "a+")
    for i in range(int(config.StartPage),int(pagenum[0])):
        print("Now write " + str(i) + " page")
        pageurl = requests.get('https://fofa.so/result?page=' + str(i) + '&qbase64=' + searchbs64, headers=config.header)
        tree = etree.HTML(pageurl.text)
        urllist=tree.xpath('//div[@class="re-domain"]//text()')
        urllist = [value.strip('\n').strip(' ').strip('\n') for value in urllist if len(value.strip('\n').strip(' ').strip('\n')) != 0]
        print(urllist)
        for j in urllist:

            print(j)
            doc.write(j+"\n")
        if i==int(config.StopPage):
            break
        time.sleep(config.TimeSleep)
    doc.close()
    print("OK,Spider is End .")


def main():
    base.logo()
    base.checkSession()
    base.init()
    spider()

if __name__ == '__main__':
    main()
