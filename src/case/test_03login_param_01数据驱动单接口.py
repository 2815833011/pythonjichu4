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
    
    @pytest.mark.parametrize('date',YamlLoad().fileload()["logindata"])
    def test_login(self,date):
        service=ChromeService(executable_path=r"driver/chromedriver")
        option=ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        driver=webdriver.Chrome(service=service,options=option)
        driver.maximize_window()
        driver.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")

        driver.implicitly_wait(10)
        driver.find_element(By.NAME,"accounts").send_keys(date[1])
        driver.find_element(By.NAME,"pwd").send_keys(date[2])
        driver.find_element(By.NAME,"verify").send_keys(date[3])
        driver.find_element(By.XPATH,"//button[text()='登录']").click()
        result=WebDriverWait(driver,10).until(lambda x :x.find_element(By.XPATH,"//*[@class='prompt-msg']")).text
        print(result)
        assert result==date[0]
        time.sleep(2)
        driver.quit()
    

        
