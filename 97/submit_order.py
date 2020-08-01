#提交订单
import json
import time
import  requests
from lxml import html
etree = html.etree
from common import base_url
from common import submit_order_path
from run import cookie
def submit_order_all(cookie:str)->dict:
    # 设置请求头信息
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    # 请求获取充值记录数据
    res = requests.get(url=base_url + submit_order_path, headers=headers)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def get_platform_name_id(url):
    r = requests.get(url)
    r.raise_for_status()
    html = etree.HTML(r.text)
    urldata_id= html.xpath("//option/@value")
    urldata_name = html.xpath("//option/text()")
    d = dict(zip(urldata_id,urldata_name))
    return d
