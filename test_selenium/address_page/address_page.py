from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver=driver
    def add_nember(self):
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
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("po封装")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("zhangtian00128")
        # 选择性别
        self.driver.find_elements(By.XPATH, "//*[@class='ww_radio']")[1].click()
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@class='qui_inputText ww_inputText ww_telInput_mainNumber']").send_keys(
            13366768877)
        # 点击保存
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[0].click()
