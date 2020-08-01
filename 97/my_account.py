#我的账户
import json
import time
import  requests
from common import base_url
from common import my_account_path
def my_account_all(cookie:str)->dict:
    # 设置请求头信息
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    data = {"id":"8888"}
    # 请求获取充值记录数据
    res = requests.post(url=base_url + my_account_path, headers=headers,params=data)
    # 如果获取到了数
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}