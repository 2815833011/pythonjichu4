from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from src.util.config import Conf
from src.util.logger import log


class Pyselenium:
    __driver=None
    __instance=None
    __aciton=None
    def __new__(cls,brower="chrome",max_window=True,timeout=10):
        if not cls.__instance:
           cls.__instance= super().__new__(cls)
           option = getattr(cls, f"{brower.lower()}option")()
           driverpath=Conf().get_driver_path(brower)
           service = getattr(cls, f"{brower.lower()}service")(driverpath)
           cls.__driver = getattr(cls, brower.lower())(option, service)
           cls.__driver.maximize_window()
           cls.__aciton = ActionChains(cls.__driver)
        return cls.__instance
    
    def __init__(self,brower="chrome",max_window=True,timeout=10):
            self.__timeout = timeout
            
            
        
    @classmethod
    def chrome(cls, option, service):

        return webdriver.Chrome(options=option, service=service)
    @classmethod
    def firefox(cls, option, service):

        return webdriver.Firefox(options=option, service=service)
    @classmethod
    def chromeoption(cls):
        from selenium.webdriver import ChromeOptions

        option = ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        return option
    @classmethod
    def firefoxoption(cls):
        from selenium.webdriver import FirefoxOptions

        option = FirefoxOptions()
        option.add_argument("--disable-notifications")  # 禁用通知弹窗
        return option
    @classmethod
    def chromeservice(cls, driverpath):
        from selenium.webdriver import ChromeService

        return ChromeService(driverpath)
    @classmethod
    def firefoxservice(cls, driverpath):
        from selenium.webdriver import FirefoxService

        return FirefoxService(driverpath)

    def getorange_driver(self):
        return self.__driver
    
    @log
    def get(self, url):
        self.__driver.get(url)

    @log
    def find_element(self, part):
        if not isinstance(part, tuple):
            raise Exception(f"*part <class={type(part)}")
        return WebDriverWait(self.__driver, self.__timeout).until(
            lambda x: x.find_element(*part)
        )
    @log
    def find_elements(self, part):
        if not isinstance(part, tuple):
            raise Exception(f"*part <class={type(part)}")
        return WebDriverWait(self.__driver, self.__timeout).until(
            lambda x: x.find_elements(*part)
        )
    @log
    def click(self, part):
        self.find_element(part=part).click()
    @log
    def send_keys(self, part, content):
        self.find_element(part=part).send_keys(content)
    @log
    def sleep(self, timeout=3):
        time.sleep(timeout)
    @log
    def switch_to_alert(self):
        alert=  alert = WebDriverWait(self.__driver, 10).until(
            EC.alert_is_present()
        )
        return alert
    @log
    def switch_to_frame(self, part=(By.TAG_NAME, "frame")):

        self.__driver.switch_to.frame(self.find_element(part))
    @log
    def switch_to_new_window(self):
        window = self.__driver.window_handles
        self.__driver.switch_to.window(window[-1])
    @log
    def switch_to_default_content(self):
        self.__driver.switch_to.default_content()
    @log
    def move_element(self, part):

        self.__aciton.move_to_element(self.find_element(part)).perform()
    @log
    def double_click(self, part):

        self.__aciton.double_click(self.find_element(part)).perform()
    @log
    def get_attribute(self, part, attribute):
        return self.find_element(part).get_attribute(attribute)

    @log
    def text(self, part):
        return self.find_element(part).text
    @log
    def wait(self, timeout=10):
        self.__driver.implicitly_wait(timeout)
    @log
    def refresh(self):
        self.__driver.refresh()
    @log
    def execute_js(self,*args):
        self.__driver.execute_script(args)
    @log
    def soll_execute_script(self,part):
        element=self.find_element(part)
        self.__driver.execute_script("arguments[0].scrollIntoView()",element)
    @log   
    def save_screenshot(self,path):
        self.__driver.save_screenshot(path)


    @log
    def get_screenshot_as_png(self):
        '''
             获取png屏幕截图
        '''
        return self.__driver.get_screenshot_as_png()

    @log
    def max_window(self):
        self.__driver.maximize_window()
    @log
    def close(self):
        self.__driver.close()
    @log
    def quit(self):
        self.__driver.quit()
    @log
    def delete_all_cookies(self):
        self.__driver.delete_all_cookies()
