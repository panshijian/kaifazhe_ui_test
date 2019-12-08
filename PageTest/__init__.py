
from selenium.webdriver.common.by import By
"""
    开发者头条 - 启动页

"""
# 定位 申请独家号
primary_btn = (By.ID,"io.manong.developerdaily:id/btn_primary")

"""
    我的页面
"""
# 定位 登录/注册
login_btn = (By.ID,"io.manong.developerdaily:id/login_btn")

"""
    登录方式 选择页面
"""
# 定位 密码登录
select_pwd_login = (By.XPATH,"//*[contains(@resource-id,'io.manong.developerdaily:id/tv_tab_title') and contains(@text,'密码登录')]")

"""
    手机号登录页面
"""
# 定位 输入手机号
input_phone = (By.ID,"io.manong.developerdaily:id/edt_phone")
# 定位 输入密码
input_phone_pwd = (By.ID,"io.manong.developerdaily:id/edt_password")
# 定位 登录按钮
phone_longin_btn = (By.ID,"io.manong.developerdaily:id/btn_login")

"""
    登录成功 个人信息页面
"""
# 定位 用户昵称
user_name = (By.ID,"io.manong.developerdaily:id/nav_tv_name")
# 定位 用户头像
img_avatar = (By.ID,"io.manong.developerdaily:id/nav_img_avatar")
# 定位 设置按钮
me_info_page_setting_btn = (By.ID,"io.manong.developerdaily:id/nav_btn_setting")
"""
    设置页面
"""
# 定位 退出当前账户
setting_page_logout_account_btn = (By.ID,"io.manong.developerdaily:id/btn_logout")
# 定位退出弹窗中的退出按钮
bounced_logout = (By.ID,"io.manong.developerdaily:id/md_buttonDefaultPositive")





