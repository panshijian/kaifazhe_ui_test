


import yaml

# data = {"Search_Data": {
#                     "search_test_002" : {"expect" : {"value" : "你好"}, "value": "你好"},
#                     "searcj_test_001" : {"wxpect" : [4,5,6], "value": 456}}}
#
# with open("./write_data.yaml", "w",encoding= 'utf-8') as f :
#     yaml.dump(data, f, encoding="utf-8", allow_unicode=True)
param_list = []
with open("./write_data.yaml","r",encoding="utf-8") as f :
    data = yaml.load(f)
    # print(data)
    # 目标[("你好"  , "你好"), (456，,456)]

    # 思路： 1 取 Search_Data值  ->2 ，取values  -> 3，再取

    for i in data.get("Search_Data").values():
        print(i)
        param_list.append((i.get("value"),i.get("expect")))
print(param_list)



"""
data = {'Search_Data': 
            {
            'search_test_002': {'expect': '你好', 'value': '你好'},
            'searcj_test_001': {'value': 456, 'wxpect': 456}}}

"""


# data = {"name" : {
#             "s1" : {"data" : 123},
#             "s2" : {"data" : 456}
# }}
#
# with open("./test_data.yaml", "w",encoding= "utf-8") as f :
#     yaml.dump(data,f,encoding = "utf-8",allow_unicode = True)