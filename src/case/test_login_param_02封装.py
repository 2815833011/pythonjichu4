import time
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.util.yamlload import YamlLoad
from src.util.pyselenium import Pyselenium
class TestLogin:
    
    def setup_class(self):
        self.pyselenium=Pyselenium()

    def setup_method(self):
        self.pyselenium.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")

    def teardown_method(self):
        self.pyselenium.delete_all_cookies()
        self.pyselenium.refresh()

    @pytest.mark.parametrize('date',YamlLoad().fileload()["logindata"])
    def test_login(self,date):

        self.pyselenium.send_keys((By.NAME,"accounts"),date[1])
        self.pyselenium.send_keys((By.NAME,"pwd"),date[2])
        self.pyselenium.send_keys((By.NAME,"verify"),date[3])
        self.pyselenium.click((By.XPATH,"//button[text()='登录']"))
        
        result=self.pyselenium.find_element((By.XPATH,"//*[@class='prompt-msg']")).text
        print(result)
        assert result==date[0]

        
