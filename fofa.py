import requests
from lxml import etree
import base64
import re
import time
import config
from urllib.parse import quote,unquote


def logo():
    print('''


             /$$$$$$$$ /$$$$$$  /$$$$$$$$ /$$$$$$                                   
            | $$_____//$$__  $$| $$_____//$$__  $$                                  
            | $$     | $$  \ $$| $$     | $$  \ $$                                  
            | $$$$$  | $$  | $$| $$$$$  | $$$$$$$$                                  
            | $$__/  | $$  | $$| $$__/  | $$__  $$                                  
            | $$     | $$  | $$| $$     | $$  | $$                                  
            | $$     |  $$$$$$/| $$     | $$  | $$                                  
            |__/      \______/ |__/     |__/  |__/                                  



                                /$$$$$$            /$$       /$$                    
                               /$$__  $$          |__/      | $$                    
                              | $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
                              |  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$
                               \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/
                               /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$      
                              |  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$      
                               \______/ | $$____/ |__/ \_______/ \_______/|__/      
                                        | $$                                        
                                        | $$                                        
                                        |__/                                        

                                                                                version:1.01
    ''')




def checkSession():
    if config.cookie=="":
        print("请配置config文件")
        exit(0)
    print("检测cookie成功")
    return




def init():
    config.TimeSleep=int(input('请输入爬取每一页等待的秒数，防止IP被ban\n'))
    config.SearchKEY = input('请输入fofa搜索关键字 \n')

    return




def spider():
    searchbs64 = quote(str(base64.b64encode(config.SearchKEY.encode()), encoding='utf-8'))

    # searchbs64 = (str(base64.b64encode(config.SearchKEY.encode('utf-8')), 'utf-8'))
    print("爬取页面为:https://fofa.info/result?qbase64=" + searchbs64)
    html = requests.get(url="https://fofa.info/result?qbase64=" + searchbs64, headers=config.headers).text
    tree = etree.HTML(html)
    try:
        pagenum = tree.xpath('//li[@class="number"]/text()')[-1]
    except Exception as e:
        print(e)
        pagenum = '0'
        pass
    # pagenum = re.findall('>(\d*)</a> <a class="next_page" rel="next"', html)
    print("该关键字存在页码: "+pagenum)
    config.StartPage=input("请输入开始页码:\n")
    config.StopPage=input("请输入终止页码: \n")
    doc = open("hello_world.txt", "a+")
    for i in range(int(config.StartPage),int(pagenum)):
        print("Now write " + str(i) + " page")
        rep = requests.get('https://fofa.info/result?qbase64=' + searchbs64+"&page="+str(i)+"&page_size=20", headers=config.headers)
        tree = etree.HTML(rep.text)
        urllist=tree.xpath('//span[@class="aSpan"]/a/@href')
        # urllist = [value.strip('\n').strip(' ').strip('\n') for value in urllist if len(value.strip('\n').strip(' ').strip('\n')) != 0]
        # pattern = re.compile('"link":"(.*?)",')
        # urllist = re.findall(pattern, rep.text)
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
    logo()
    checkSession()
    init()
    spider()




if __name__ == '__main__':
    main()
