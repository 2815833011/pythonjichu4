
from selenium.webdriver.common.by import By


class ShopInto:
    def __init__(self,pyselenium):
        self.pyselenium=pyselenium
        self.imbuy=(By.XPATH,"//*[contains(text(),'立即购买')]")
    
    def click_tobuy(self):
        self.pyselenium.click(self.imbuy)
        
