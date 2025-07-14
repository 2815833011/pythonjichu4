import time
import pytest
from selenium.webdriver.common.by import By
from src.util.pyselenium import Pyselenium
from selenium.webdriver.support.select import Select
class TestLogin:
    
    def setup_class(self):
        self.pyselenium=Pyselenium()

    def teardown_method(self):
        self.pyselenium.delete_all_cookies()
        self.pyselenium.refresh()

    @pytest.mark.usefixtures("login_fix")
    def test_login(self):
        self.pyselenium.click((By.XPATH,"//*[text()='商城首页']"))
        self.pyselenium.wait(10)
        self.pyselenium.click((By.XPATH,"//a[starts-with(text(),'华为畅享')]"))
        self.pyselenium.switch_to_new_window()
        self.pyselenium.wait(10)
        self.pyselenium.click((By.XPATH,"//*[contains(text(),'立即购买')]"))
        self.pyselenium.save_screenshot("report/buy.png")
        self.pyselenium.click((By.XPATH,"//*[contains(text(),'添加新地址')]"))
        self.pyselenium.switch_to_frame((By.XPATH,"//iframe[@class='am-block']"))
        self.pyselenium.send_keys((By.XPATH,"//*[@name='name']"),"tangying")
        self.pyselenium.send_keys((By.XPATH,"//*[@name='alias']"),"tangying")
        self.pyselenium.send_keys((By.XPATH,"//*[@name='tel']"),"17673415861")
        self.pyselenium.click((By.XPATH,"//span[text()='省份']"))
        self.pyselenium.click((By.XPATH,"//li[text()='河北省']"))
        self.pyselenium.click((By.XPATH,"//span[text()='城市']"))
        self.pyselenium.click((By.XPATH,"//li[text()='唐山市']"))
        self.pyselenium.click((By.XPATH,"//span[text()='区/县']"))
        self.pyselenium.click((By.XPATH,"//li[text()='路北区']"))
        self.pyselenium.send_keys((By.XPATH,"//*[@name='address']"),"fsdfaefasdfaefsfe")
        self.pyselenium.click((By.XPATH,"//span[text()='保存']"))
        time.sleep(5)
        self.pyselenium.switch_to_default_content()
        self.pyselenium.click((By.XPATH,"//span[text()='现金支付']"))
        self.pyselenium.click((By.XPATH,"//*[@class='go-btn-wrap']/button/span"))

        
        
