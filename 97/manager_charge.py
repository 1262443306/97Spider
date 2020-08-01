#代理管理
import json
import time
import  requests
from common import base_url
from common import manager_charge_path
from common import open_manager_account_path
from common import open_manager_right_path,change_price_path,recharge_to_manager_path
def manager_charge_all(cookie:str)->dict:
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
    res = requests.get(url=base_url + manager_charge_path + str(timestamp_haomiao), headers=headers)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def open_manager_account_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "status":"1"    }
    res = requests.post(url=base_url + open_manager_account_path, headers=headers,params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def stop_manager_account_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "status": "0"}
    res = requests.post(url=base_url + open_manager_right_path, headers=headers, params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def close_manager_right_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "is_parent":"0"}
    res = requests.post(url=base_url + open_manager_right_path, headers=headers, params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def open_manager_right_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "status": "1"}
    res = requests.post(url=base_url + open_manager_right_path, headers=headers, params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def change_price_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "price": "0.006"}
    res = requests.post(url=base_url + change_price_path, headers=headers, params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}
def recharge_to_manager_all(cookie:str)->dict:
    headers = {
        "Referer": base_url,
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Cookie": "PHPSESSID=" + cookie
    }
    params = {
        "id": "43941",
        "amount": "0.001"}
    res = requests.post(url=base_url + recharge_to_manager_path, headers=headers, params=params)
    # 如果获取到了数据
    if not res.text is None:
        # 将数据转化为json数据即字典数据
        dict_text = json.loads(res.text)
        return dict_text
    return {'status': 1, 'message': '没有获取到数据'}