from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
'''
conf
data
driver
log
report
src
    case
    po
    util

'''

class TestIndex:
    def test_search(self):
        '''
            测试搜索功能
        '''

        service=ChromeService(executable_path=r"driver/chromedriver")
        option=ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        driver=webdriver.Chrome(service=service,options=option)
        driver.maximize_window()
        driver.get("http://www.liuyanzu.tech/shopxo/")

        driver.implicitly_wait(10)
        driver.find_element(By.ID,"search-input").send_keys("遥遥领先")
        driver.find_element(By.ID,"ai-topsearch").click()
        driver.implicitly_wait(10)
        result=driver.find_element(By.XPATH,"//*[text()='没有相关数据']").text
        assert result=="没有相关数据"