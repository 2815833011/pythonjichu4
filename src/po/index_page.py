
from selenium.webdriver.common.by import By


class IndexPage:
    def __init__(self,pyselenium):
        self.pyselenium=pyselenium
        self.indexbtn=(By.XPATH,"//*[text()='商城首页']")
        self.link=(By.XPATH,"//a[starts-with(text(),'华为畅享')]")

    def click_tobuy(self):
        self.pyselenium.click(self.indexbtn)
        self.pyselenium.wait()
        self.pyselenium.click(self.link)
