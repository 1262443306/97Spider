import json
import time

import  requests
base_url="http://daikan.wbs.im/"
login_path="user/login"
code_path="user/code"
#查询订单
wk_order_path="data/get?method=customer/getlist&offset=0&_="
#批量提交
submit_order_path = "customer/submit"
#批量提交平台名字获取
platform_name_id_path="customer/create"
#提交结果
submit_order_result_path="data/get?method=customer/getqueue&_="
#课程查询
course_search_path="data/get?method=customer/toolquery"
#加入订单
add_course_order_path ="customer/toolsubmit"
#代理管理
manager_charge_path = "data/get?method=customer/managelist&_="
#代理账户开启,#停用代理账户权限
open_manager_account_path = "customer/manageset"
#代理权限开启，#关闭代理权限
open_manager_right_path ="customer/manageright"
#改变代理价格
change_price_path = "customer/manageprice"
#给代理充值
recharge_to_manager_path="customer/managepay"
#在线充值
recharge_online_path="data/get?method=customer/getbill&_="
recharge_online_money_path = "data/get?method=customer/calculate"
#我的账户
my_account_path = "customer/getnotice"
#订单查找
order_serach_path = "customer/searchcourse"
money_to_client_path = "customer/managepay"
spend_order_path = "data/get?method=customer/getbill&_="
residue_money_path = "data/get?method=customer/calculate"
order_search_path="customer/searchcourse"
pay_order_path="data/get?method=customer/getbill&_="