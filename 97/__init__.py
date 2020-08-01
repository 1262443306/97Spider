from run import login
from search_order import get_order_all
from submit_order import submit_order_all,get_platform_name_id
import common
from course_search import course_search_all,add_course_order_all
from submit_order_result import submit_order_result_all
from manager_charge import manager_charge_all,open_manager_account_all,stop_manager_account_all,close_manager_right_all,open_manager_right_all,change_price_all,recharge_to_manager_all
from run import cookie,base_url
from recharge_online import recharge_online_all,recharge_online_money_all
from my_account import my_account_all
from order_search import order_search_all

# from run import user,password
#
# login(user,password)
result = get_order_all(cookie)
print("查询订单:",result)
result = submit_order_all(cookie)
print("批量提交:",result)
result = submit_order_result_all(cookie)
print("提交结果:",result)
result = course_search_all(cookie)
print("课程查询:",result)
result = manager_charge_all(cookie)
print("代理管理:",result)
result = recharge_online_all(cookie)
print("在线充值流水具体情况:",result)
result = recharge_online_money_all(cookie)
print("在线充值流水总情况:",result)
result = my_account_all(cookie)
print("我的账户:",result)
result = order_search_all(cookie)
print("订单查找:",result)
result = open_manager_account_all(cookie)
print("打开代理账户:",result)
result = stop_manager_account_all(cookie)
print("暂停代理账户:",result)
result = close_manager_right_all(cookie)
print("关闭代理权限:",result)
result = open_manager_right_all(cookie)
print("打开代理权限:",result)
result = change_price_all(cookie)
print("改变价格:",result)
result = recharge_to_manager_all(cookie)
print("给代理充值:",result)
result = add_course_order_all(cookie)
print("加入订单:",result)
result = get_platform_name_id(base_url+common.platform_name_id_path)
print("APPid与名字:",result)
