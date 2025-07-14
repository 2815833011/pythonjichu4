import os,sys
sys.path.append(os.getcwd())
import pytest
from src.util.pyselenium import Pyselenium
from src.util.yamlload import YamlLoad
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def login_fix():
    pyselenium=Pyselenium()
    pyselenium.get("http://www.liuyanzu.tech/shopxo/?s=user/logininfo.html")
    date=YamlLoad().fileload()["logindata"]
    pyselenium.wait(10)
    pyselenium.send_keys((By.NAME,"accounts"),date[0][1])
    pyselenium.send_keys((By.NAME,"pwd"),date[0][2])
    pyselenium.send_keys((By.NAME,"verify"),date[0][3])
    pyselenium.click((By.XPATH,"//button[text()='登录']"))
    time.sleep(2)
    result=pyselenium.find_element((By.XPATH,"//*[@class='prompt-msg']")).text
    print(result)
    assert result==date[0][0]
    alert=pyselenium.switch_to_alert()
    alert.accept()
    time.sleep(5)
    


    

    