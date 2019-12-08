import PageTest
from BaseTest.basetest import Base

class Page_Dev(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)
        self.scoll_size = self.driver.get_window_size()

    def scoll_left(self):
        # 'width': int(width), 'height': int(height)
        # 启动页 连续滑动3次
        try:
            self.driver.swipe(self.scoll_size.get("width")*0.9,self.scoll_size.get("height")*0.5,
                              self.scoll_size.get("width") * 0.1, self.scoll_size.get("height") * 0.5,1000)

        except Exception as e:
            print(e)
            return False

    def click_primary(self):
        # 点击 申请独家号
        self.click_element(PageTest.primary_btn)

    def click_login_btn(self):
        # 点击 登录/注册
        self.click_element(PageTest.login_btn)

    def select_login_mode(self):
        # 选择手机登录 - 点击密码登录
        self.click_element(PageTest.select_pwd_login)

    def input_phone_pwd(self,phone,pwd):
        # 输入 手机号
        self.input_element(PageTest.input_phone,phone)
        # 输入密码
        self.input_element(PageTest.input_phone_pwd,pwd)

    def click_phone_login_btn(self):
        # 点击 手机号登录页面 的 登录按钮
        self.click_element(PageTest.phone_longin_btn)

    def expect_name(self):
        # 获取用户昵称的文本信息
        return self.search_element(PageTest.user_name).text

    def scoll_up(self):
        # 向上滑动 80%  ---> 30 %
        try:
            self.search_element(PageTest.img_avatar)
            self.driver.swipe(self.scoll_size.get("width")*0.5,self.scoll_size.get("height")*0.8,
                              self.scoll_size.get("width") * 0.5, self.scoll_size.get("height") * 0.3,1000)
        except Exception as e :
            print(e)
            return False

    def scoll_down(self):
        # 向下滑动 30% ---->80%
        try:
            self.search_element(PageTest.me_info_page_setting_btn)
            self.driver.swipe(self.scoll_size.get("width") * 0.5, self.scoll_size.get("height") * 0.3,
                              self.scoll_size.get("width") * 0.5, self.scoll_size.get("height") * 0.8, 1000)

        except Exception as e :
            print(e)
            return False
    def click_setting_btn(self):
        # 点击 我的页面 设置按钮
        self.click_element(PageTest.me_info_page_setting_btn)

    def click_setting_page_logout_btn(self,type_out ):
        # 点击 设置页面 退出当前账号 按钮
        self.click_element(PageTest.setting_page_logout_account_btn)
        # type_out : 1 点击退出  type_out :2 点击取消
        if type_out == 2:
            self.click_element(PageTest.bounced_logout)

    def phone_login_text(self):
        # 获取登录失败 的 登录文本

        return self.search_element(PageTest.phone_longin_btn).text
