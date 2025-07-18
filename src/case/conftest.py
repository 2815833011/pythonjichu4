import os,sys
sys.path.append(os.getcwd())
import pytest
from src.util.pyselenium import Pyselenium
from src.util.yamlload import YamlLoad
from selenium.webdriver.common.by import By
import time
from src.po.login_page import LoginPage

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



#pom buy 前提条件 夹具
@pytest.fixture(params=[["tangying",123456,"A1B2"]])
def login_fixpom(request):
    loginpage=LoginPage()
    loginpage.navigets()
    loginpage.login(*request.param)
    loginpage.whether("登录成功")


def pytest_terminal_summary(terminalreporter,exitstatus,config):
    '''

    '''
    passmd,fail,skip=[],[],[]
    for status,reports in terminalreporter.stats.items():
           '''
           terminalreporter 主要参数
            status 状态
            reports 用例详情
           '''
           match status:
                case "passed":
                     for report in reports:
                          nodeid =report.nodeid
                          reason =report.longreprtext
                          passmd.append({nodeid:reason})
                case "failed":
                     for report in reports:
                          nodeid =report.nodeid
                          reason =report.longreprtext
                          fail.append({nodeid:reason})
                case "skipped":
                     for report in reports:
                          nodeid =report.nodeid
                          reason =report.longreprtext
                          skip.append({nodeid:reason})
    return passmd,fail,skip
    
    

    


    

    