import requests
import re
url='https://api.fofa.so/v1/search?qbase64=Iua1i%2BivlSI%3D&full=false&pn=2&ps=10'

headers = {
        "Connection": "keep-alive",
        "Authorization": "eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6ODE0LCJtaWQiOjEwMDAwMzIyMywidXNlcm5hbWUiOiIweDU4NEEiLCJleHAiOjE2MTc1NjY2MDF9.IMHI3ksyrscqGbc8Qw9Ki3ONepl3u6pinEbT_SkUMIcsfpNUhoy0j0LV4-MAqDL5hZE_ekZQkBjDzcq4U3nB3w",
    }

rep=requests.get(url,headers=headers)
pattern = re.compile('"link":"(.*?)",')
result=re.findall(pattern,rep.text)
print(result)