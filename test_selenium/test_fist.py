import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwars:
    def setup(self):
        # 初始化driver
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        # 打开网址
        self.driver.get("https://www.baidu.com")
        #向搜索框输入，搜索内容【霍格沃兹测试学院】
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        time.sleep(1)
        self.driver.find_element(By.ID,"su").click()
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页")





