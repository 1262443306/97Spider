#提交订单结果查询
import json
import time

import  requests
from common import base_url
from common import submit_order_result_path
from run import cookie
def submit_order_result_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    # 生成时间戳
    timestamp_miao = time.time()  # 秒时间戳
    timestamp_haomiao = int(round(timestamp_miao * 1000))  # 毫秒时间戳
    params = {
        "_": timestamp_haomiao
    }
    res = requests.get(url=base_url + submit_order_result_path + str(timestamp_haomiao), headers=headers)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}