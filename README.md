# Fofa-python-脚本
### 起因

使用关键字在`fofa`上查询后，手动测试fofa上面每一个链接，并且进行漏洞测试着实麻烦，但`fofa`的`API`又是要收费的，所以很容易会想到使用爬虫进行链接爬取

### 简介

基于`python3`的`fofa`爬取

爬取的链接会存储在`hello_world.txt`

默认每隔`5`秒爬取一页数据

### 下载

`git clone https://github.com/Cl0udG0d/Fofa-script`

### 使用

配置`config.py`中的`cookie`

运行`fofa.py`

> python3 fofa.py

### 原理

https://www.cnblogs.com/Cl0ud/p/14324445.html

### logo

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



### 更新日志

+ 2021-4-4 对最新版`fofa`更新做出对应更新，注意：`config.py`文件中不再是以`cookie`来进行保证登录，而是使用`Authorization`，`Authorization`的值可以登录后`F12`在`https://api.fofa.so/v1/search`网址请求头中看到

  ![](https://github.com/Cl0udG0d/Fofa-script/blob/master/images/1.png)
  
+ 2021-8-28 对 [issue5](https://github.com/Cl0udG0d/Fofa-script/issues/5) 提出的问题进行修改

  感谢 [yq1ng](https://github.com/yq1ng)  指出问题与解决方案
+ 2022-2-26 由于众所周知的原因，原fofa.so网址已无法查询，更改爬取网站为fofa.info，配置config文件中的cookie进行使用即可（cookie的位置打开F12查看请求头即可看到）

### END 
 
建了一个微信的安全交流群，欢迎添加我微信备注`进群`，一起来聊天吹水哇，以及一个会发布安全相关内容的公众号，欢迎关注 :)
 
<div>
    <img  alt="GIF" src="https://springbird.oss-cn-beijing.aliyuncs.com/img/mmqrcode1632325540724.png"  width="280px" />
    <img  alt="GIF" src="https://springbird.oss-cn-beijing.aliyuncs.com/img/qrcode_for_gh_cead8e1080d6_344.jpg"  width="280px" />
</div>