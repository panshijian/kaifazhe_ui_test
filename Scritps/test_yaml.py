import  pytest, os, sys
# sys.path.append(os.getcwd())
proj_path = os.path.dirname(os.getcwd())
sys.path.append(proj_path)
print(proj_path)
from BaseTest.read_data import Op_Data



def get_yml_data():
    # 读取yaml文件
    data_list = []
    # with open(os.getcwd()+os.sep+"Data"+os.sep+"test_data.yaml", "r") as f:
    #     data = yaml.load(f).get("Search_Data")
    # 读yaml数据
    data = Op_Data("t_data.yaml").read_yaml().get("Search_Data")
    for i in data.values():
        data_list.append((i.get("input"), i.get("expect")))
    return data_list

class Test_yaml:

    # def get_pathx(self):
    #     print("当前路径:",os.getcwd())

    # [(input,expect)]
    @pytest.mark.parametrize("input_data, expect_data", get_yml_data())
    def test_001(self, input_data, expect_data):
        # 输入 == 预期结果
        # self.get_pathx()
        # base_path()
        assert input_data == expect_data
