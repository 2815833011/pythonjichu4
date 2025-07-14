import time
from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'''
单接口用例
'''
class Testlogim:
    def test_login_success(self):
        service=ChromeService(executable_path=r"driver/chromedriver")
        option=ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        driver=webdriver.Chrome(service=service,options=option)
        driver.maximize_window()
        driver.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")
        
        driver.implicitly_wait(10)
        driver.find_element(By.NAME,"accounts").send_keys("tangying")
        driver.find_element(By.NAME,"pwd").send_keys(123456)
        driver.find_element(By.NAME,"verify").send_keys("A1B2")
        driver.find_element(By.XPATH,"//button[text()='登录']").click()
        result=WebDriverWait(driver,10).until(lambda x :x.find_element(By.XPATH,"//*[@class='prompt-msg']")).text
        assert result=="登录成功"

        
    def test_login_errpwd(self):
        service=ChromeService(executable_path=r"driver/chromedriver")
        option=ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        driver=webdriver.Chrome(service=service,options=option)
        driver.maximize_window()
        driver.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")

        driver.implicitly_wait(10)
        driver.find_element(By.NAME,"accounts").send_keys("tangying")
        driver.find_element(By.NAME,"pwd").send_keys(123457)
        driver.find_element(By.NAME,"verify").send_keys("A1B2")
        driver.find_element(By.XPATH,"//button[text()='登录']").click()
        result=WebDriverWait(driver,10).until(lambda x :x.find_element(By.XPATH,"//*[@class='prompt-msg']")).text
        assert result=="密码错误"


    def test_login_errcode(self):
        service=ChromeService(executable_path=r"driver/chromedriver")
        option=ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        driver=webdriver.Chrome(service=service,options=option)
        driver.maximize_window()
        driver.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")

        driver.implicitly_wait(10)
        driver.find_element(By.NAME,"accounts").send_keys("tangying")
        driver.find_element(By.NAME,"pwd").send_keys(123456)
        driver.find_element(By.NAME,"verify").send_keys("A1B1")
        driver.find_element(By.XPATH,"//button[text()='登录']").click()
        result=WebDriverWait(driver,10).until(lambda x :x.find_element(By.XPATH,"//*[@class='prompt-msg']")).text
        assert result=="验证码错误"

    