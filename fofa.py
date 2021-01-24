import requests
from lxml import etree
import base64
import re
import time

cookie = ''


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
                                
                                                                                version:1.0
    ''')


def spider():
    header = {
        "Connection": "keep-alive",
        "Cookie": "_fofapro_ars_session=" + cookie,
    }
    search = input('please input your key: \n')
    searchbs64 = (str(base64.b64encode(search.encode('utf-8')), 'utf-8'))
    print("spider website is :https://fofa.so/result?&qbase64=" + searchbs64)
    html = requests.get(url="https://fofa.so/result?&qbase64=" + searchbs64, headers=header).text
    pagenum = re.findall('>(\d*)</a> <a class="next_page" rel="next"', html)
    print("have page: "+pagenum[0])
    stop_page=input("please input stop page: \n")
    #print(stop_page)
    doc = open("hello_world.txt", "a+")
    for i in range(1,int(pagenum[0])):
        print("Now write " + str(i) + " page")
        pageurl = requests.get('https://fofa.so/result?page=' + str(i) + '&qbase64=' + searchbs64, headers=header)
        tree = etree.HTML(pageurl.text)
        urllist=tree.xpath('//div[@class="re-domain"]/text()')
        for j in urllist:
            print(j.strip())
            doc.write(j.strip()+"\n")
        if i==int(stop_page):
            break
        time.sleep(5)
    doc.close()
    print("OK,Spider is End .")

def start():
    print("Hello!My name is Spring bird.First you should make sure _fofapro_ars_session!!!")
    print("And time sleep is 10s")

def main():
    logo()
    start()
    spider()

if __name__ == '__main__':
    main()
