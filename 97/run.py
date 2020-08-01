#登录
import json
import os
import time

import  requests


base_url="http://daikan.wbs.im/"
login_path="user/login"
code_path="user/code"


def login(user,password)->list:
    cookie=''
    fail=0
    while(True):
        try:
            res=requests.get(url=base_url)
            print(res.cookies)
            if not res.status_code==200:
                print("请求错误！")
                return
            #global cookie
            cookie=res.cookies["PHPSESSID"]
            break
        except:
            fail+=1
            if fail<=3:
                time.sleep(1)
            else:
                print("尝试五次连接失败！")
                raise
                return
    print(cookie)

    #获取验证码
    headers={
        "Referer":base_url,
        #"User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie":"PHPSESSID="+cookie
    }
    timestamp_miao=time.time() #秒时间戳
    timestamp_haomiao=int(round(timestamp_miao*1000)) #毫秒时间戳
    params={
        "_":timestamp_haomiao
    }
    print(params["_"])
    #获取验证码，放在一个文件中
    res=requests.post(url=base_url+code_path,headers=headers,params=params)
    read_dir = os.path.join(os.curdir, 'read')
    if not os.path.isdir(read_dir):
        os.mkdir(read_dir)
    filepath = os.path.join(read_dir,"img_code.jpg")
    with open(filepath,"wb+") as file:
        file.write(res.content)
    code=input("输入验证码：")
    params={
        "recommender": "0",
        "type": "1",
        "platform": "1",
        "school":"",
        "user": user,
        "password": password,
        "code": code
    }

    res=requests.post(url=base_url+login_path,params=params,headers=headers,allow_redirects=False)
    #res.encoding="json"
    if res.status_code==302:
        print("登录成功，您的cookie为:",(cookie))

    else:
        dict_text = json.loads(res.text)
        print(dict_text)
    return cookie


# user = input("请输入账号：")
# password = input("请输入密码：")
# login(user,password)
cookie = "qmova5usoqi5o0b6p2i7na6cu2"
