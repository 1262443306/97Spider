#课程查询
import json
import time
import  requests
from common import base_url
from common import course_search_path,add_course_order_path
from run import cookie
def course_search_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    data = {"id":"NDljMDUwbmyWbpxumA=="}
    res = requests.post(url=base_url + course_search_path , headers=headers,data=data)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def add_course_order_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    data = {"courseids": "54699730"}
    res = requests.post(url=base_url + add_course_order_path , headers=headers,data=data)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}