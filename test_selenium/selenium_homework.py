import json
from http import cookies
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    def setup(self):
        """
        复用浏览器登录
        :return:
        """
        # 声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:1000'
        # 打开驱动、隐式等待
        self.driver=webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        # 关闭浏览器
        self.driver.quit()
    def test_main_tmp(self):
        """
        基于企业微信首页登录
        :return:
        """
        # 打开浏览器、定位元素
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH,"//*[@class='index_top_operation_loginBtn']").click()
        # self.driver.find_element(By.XPATH,"//*[@class='login_registerBar_link']").click()
        # self.driver.find_element(By.XPATH,"//*[@class='qui_inputText ww_inputText ww_inputText_Big']").send_keys("张志强")
        # sleep(3)
        # self.driver.close()
    def test_longin_tmp(self):
        """
        基于浏览器复用后的内容登录
        :return:
        """
        # 声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:1000'
        # 打开驱动、隐式等待
        self.driver = webdriver.Chrome(options=chrome_arg)
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # self.driver.find_element(By.XPATH,"//*[@class='frame_nav_item']").click()

        # a = self.driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")
        # print(len(a))

        # 不可交互
        # 1.元素被遮挡:元素面前还有其它不可见元素；
        # 2.元素有多个，需要人工选择合适的元素；
        def wait_name(driver):
            driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            eles = driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_name)
        # self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("张天")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("zhangtian00124")
        # 选择性别
        self.driver.find_elements(By.XPATH, "//*[@class='ww_radio']")[1].click()
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@class='qui_inputText ww_inputText ww_telInput_mainNumber']").send_keys(13366768895)
        # 点击保存
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[0].click()

    def test_cookie_login(self):
        # 存入cookies
        # cookies=self.driver.get_cookies()
        # with open("tmp.txt","w",encoding="utf-8") as f:
        #     json.dump(cookies,f)
        #     f.write(json.dumps(cookies))
        # print(cookies)

        # 读取cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp.txt","r",encoding="utf-8") as f:
            raw_cookies= f.read()
        #     序列化:对象转化成文本； 反序列化：文本转化成对象
        cookies = json.loads(raw_cookies)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)


