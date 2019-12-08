from appium import webdriver

def get_driver(ack, act):
    desired_caps = {}
    # 平台
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "4.3"
    # 手机设备名称
    desired_caps["deviceName"] = "4df7eb4a16823055"
    # app包名
    desired_caps["appPackage"] = ack
    # app启动名
    desired_caps["appActivity"] = act
    desired_caps['autoGrantPermissions'] = True
    # 允许中文输入
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeybobard"] = True
    # 接收启动参数接
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)