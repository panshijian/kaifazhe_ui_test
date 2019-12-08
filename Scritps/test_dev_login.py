import pytest,os,sys
proj_path = os.path.dirname(os.getcwd())
sys.path.append(proj_path)
from BaseTest.init_driver import get_driver
from PageTest.dev_title import Page_Dev
from BaseTest.read_data import Op_Data

def get_data_yaml():
    data_list = []
    data = Op_Data('dev_login_data.yaml').read_yaml().get("Dev_login")
    print(data)
    for i in data:
        data_list.append((i.get("login_phone").get("phone"),i.get("login_phone").get("pwd"),i.get("login_phone").get("expect")))
        # data_list.append((i.get("phone"),i.get("pwd"),i.get("expect")))
    return data_list


class Test_Dev_Login:

    def setup_class(self):
        self.DL = Page_Dev(get_driver("io.manong.developerdaily","io.toutiao.android.ui.activity.LaunchActivity"))
        # 使用 首页启动连续从右往左滑动方法
        for i in range(3):
            self.DL.scoll_left()
        # 使用首页 点击申请独家号 按钮方法
        self.DL.click_primary()
    def teardown_class(self):
        self.DL.driver.quit()

    @pytest.mark.parametrize("phone,pwd,expect",get_data_yaml())
    def test_login(self,phone,pwd,expect):
        # 使用 点击登录/注册 按钮方法
        self.DL.click_login_btn()
        # 使用 登录方式选择 - 密码登录
        self.DL.select_login_mode()
        # 使用 输入手机号和密码的方法
        self.DL.input_phone_pwd(phone,pwd)
        # 使用 点击手机号 登录页面 登录按钮
        self.DL.click_phone_login_btn()
        # 使用 获取用户昵称文本 的方法 ，并判断是否符合预期结果
        assert expect in self.DL.expect_name(),self.DL.get_screen()
        # 使用 向上滑动方法
        self.DL.scoll_up()
        # 使用 点击设置按钮 方法
        self.DL.click_setting_btn()
        # 使用 点击退出弹框中的退出按钮 方法
        self.DL.click_setting_page_logout_btn(type_out=2)
        # 使用 向下滑动方法
        self.DL.scoll_down()

    @pytest.mark.parametrize("phone,pwd,expect", get_data_yaml())
    def test_failure(self,phone,pwd,expect):
        # 使用 点击登录/注册 按钮方法
        self.DL.click_login_btn()
        # 使用 登录方式选择 - 密码登录
        self.DL.select_login_mode()
        # 使用 输入手机号和密码的方法
        self.DL.input_phone_pwd(phone, pwd)
        # 使用 点击手机号 登录页面 登录按钮
        self.DL.click_phone_login_btn()

        assert expect == self.DL.expect_name(),self.DL.get_screen()


