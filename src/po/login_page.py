'''
po 模式 pageobject.  页面对象存储模式
按照页面为单位，使用类来封装页面元素 与动作
在测试用例中 只需要实例话类就能实现页面执行 
'''
from selenium.webdriver.common.by import By
from src.util.pyselenium import Pyselenium
import time
class LoginPage:
    
    #封装元素
    def __init__(self):
        self.pyselenium=Pyselenium()
        self.accounts=(By.NAME,"accounts")
        self.password=(By.NAME,"pwd")
        self.verify=(By.NAME,"verify")
        self.login_btn=(By.XPATH,"//button[text()='登录']")
        self.prompt=(By.XPATH,"//*[@class='prompt-msg']")
    
    def navigets(self):
        self.pyselenium.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")
    
    def login(self,account,pas,verfiycode):
        self.pyselenium.send_keys(self.accounts,account)
        self.pyselenium.send_keys(self.password,pas)
        self.pyselenium.send_keys(self.verify,verfiycode)
        self.pyselenium.click(self.login_btn)

    def whether(self,real):
        result=self.pyselenium.find_element(self.prompt).text
        assert result==real
        time.sleep(5)