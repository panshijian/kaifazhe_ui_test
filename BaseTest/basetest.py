import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):
        # 初始化driver
        self.driver = driver

    def search_element(self,loc,timeout = 15):
        """
        定位单个元素 - 显示等待
        :param loc: 元组(定位类型，类型属性) 例：(By.ID,"ID属性值")
        :param timeout: 显示等待时间
        :return:
        """
        return WebDriverWait(self.driver,timeout).until(lambda x : x.find_element(*loc))

    def search_elements(self,loc,timeout = 15):
        """
        定位一组元素 - 显示等待
        :param loc: 元组(定位类型，类型属性) 例：(By.ID,"ID属性值")
        :param timeout: 显示等待时间
        :return:
        """
        return WebDriverWait(self.driver,timeout).until(lambda x : x.find_elements(*loc))

    def click_element(self,loc):
        # 元素点击方法
        self.search_element(loc).click()

    def click_elements(self,loc,num):
        # 一组元素通过 index = []的方法点击
        list_elements = self.search_elements(loc)
        list_elements[num].click()

    def input_element(self,loc,text):
        # 输入文本信息
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)

    def get_screen(self):
        self.driver.get_screenshot_as_file("./Screen/%s.png" % time.time())

