# import yaml
# # with open("./data.yaml","r") as f :
# #     data = f.read()
# #     print(type(data))
# #     print(data)
# # yaml文件冒号后面一定跟空格，不然解析出来就是字符串
# with open("./data.yaml","r",encoding="utf-8") as f :
#     # 读取文件
#     data = yaml.load(f)
# print(type(data))
# print(data)
# # 获取value值
# print(type(data.get("data")))

# pwd_data = data.get("data").get("data_int")
#
# print(type(pwd_data))
# print(pwd_data)

# data_true = data.get("data_bool").get("data_true")
#
# data_false = data.get("data_bool").get("data_false")
#
# print(type(data_true))
# print("data_true: ",data_true)
# print(type(data_false))
# print("data_false:" ,data_false)

# print(type(data.get("data_null").get("null_01")))
# print(data)

# print(type(data.get("data_data").get("ymd")))
# print(type(data.get("data_data").get("ymdhms")))
# print(data)

import os, sys

proj_path = os.path.dirname(os.getcwd())
sys.path.append(proj_path)


import BaseTest
BaseTest.base_path()
from BaseTest.read_data import Op_Data
# print(proj_path)
def get_data():
    data_list = []
    data = BaseTest.Op_Data('dev_login_data.yaml').read_yaml().get("Dev_login")
    print(data)
    for i in data:
        data_list.append((i.get("login_phone").get("phone"), i.get("login_phone").get("pwd"), i.get("login_phone").get("expect")))
        print(data_list)
get_data()
