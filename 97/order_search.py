#订单查找
import json
import time

import  requests
from common import base_url
from common import order_search_path
def order_search_all(cookie:str)->dict:
    # 设置请求头信息
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {"account": "201806010207"}
    # 请求获取充值记录数据
    res = requests.get(url=base_url + order_search_path, headers=headers,params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}