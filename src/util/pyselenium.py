from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


class Pyselenium:
    __driver=None
    __instance=None
    __aciton=None
    def __new__(cls,brower="chrome",max_window=True,driverpath=r"driver/chromedriver",timeout=10):
        if not cls.__instance:
           cls.__instance= super().__new__(cls)
           option = getattr(cls, f"{brower.lower()}option")()
           service = getattr(cls, f"{brower.lower()}service")(driverpath)
           cls.__driver = getattr(cls, brower.lower())(option, service)
           cls.__driver.maximize_window()
           cls.__aciton = ActionChains(cls.__driver)
        return cls.__instance
    
    def __init__(self,brower="chrome",max_window=True,driverpath=r"driver/chromedriver",timeout=10):
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
        option.add_experimental_option("prefs",{"credentials_enable_service":False,"profile.password_manager_enabled":False})
        option.add_argument("--ignore-certificate-errors")  # 忽略证书错误
        option.add_argument("--accept-insecure-certs")  # 接受不安全的证书
        option.add_argument("--disable-infobars")  # 禁止“Chrome正受到自动软件控制”的提示
        option.add_argument("--disable-save-password-bubble")  # 禁止保存密码弹窗
        option.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
        })
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

    def get(self, url):
        self.__driver.get(url)

    def find_element(self, part):
        if not isinstance(part, tuple):
            raise Exception(f"*part <class={type(part)}")
        return WebDriverWait(self.__driver, self.__timeout).until(
            lambda x: x.find_element(*part)
        )

    def find_elements(self, part):
        if not isinstance(part, tuple):
            raise Exception(f"*part <class={type(part)}")
        return WebDriverWait(self.__driver, self.__timeout).until(
            lambda x: x.find_elements(*part)
        )

    def click(self, part):
        self.find_element(part=part).click()

    def send_keys(self, part, content):
        self.find_element(part=part).send_keys(content)

    def sleep(self, timeout=3):
        time.sleep(timeout)

    def switch_to_alert(self):
        alert=  alert = WebDriverWait(self.__driver, 10).until(
            EC.alert_is_present()
        )
        return alert

    def switch_to_frame(self, part=(By.TAG_NAME, "frame")):

        self.__driver.switch_to.frame(self.find_element(part))

    def switch_to_new_window(self):
        window = self.__driver.window_handles
        self.__driver.switch_to.window(window[-1])

    def switch_to_default_content(self):
        self.__driver.switch_to.default_content()

    def move_element(self, part):

        self.__aciton.move_to_element(self.find_element(part)).perform()

    def double_click(self, part):

        self.__aciton.double_click(self.find_element(part)).perform()

    def get_attribute(self, part, attribute):
        return self.find_element(part).get_attribute(attribute)

    @property
    def text(self, part):
        return self.find_element(part).text

    def wait(self, timeout=10):
        self.__driver.implicitly_wait(timeout)

    def refresh(self):
        self.__driver.refresh()

    def execute_js(self,*args):
        self.__driver.execute_script(args)
    
    def soll_execute_script(self,part):
        element=self.find_element(part)
        self.__driver.execute_script("arguments[0].scrollIntoView()",element)
        
    def save_screenshot(self,path):
        self.__driver.save_screenshot(path)

    def max_window(self):
        self.__driver.maximize_window()

    def close(self):
        self.__driver.close()

    def quit(self):
        self.__driver.quit()

    def delete_all_cookies(self):
        self.__driver.delete_all_cookies()
