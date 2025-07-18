
from selenium.webdriver.common.by import By


class ShopPay:

    def __init__(self,pyselenium):
        self.pyselenium=pyselenium
        self.imbuy=(By.XPATH,"//*[contains(text(),'立即购买')]")
        self.add_address_btn=(By.XPATH,"//*[contains(text(),'添加新地址')]")
        self.iframe=(By.XPATH," //iframe[@class='am-block']")
        self.name=(By.XPATH,"//*[@name='name']")
        self.alias=(By.XPATH,"//*[@name='alias']")
        self.tel=(By.XPATH,"//*[@name='tel']")
        self.arae=(By.XPATH,"//span[text()='省份']")
        self.arae2=(By.XPATH,"//li[text()='河北省']")
        self.city=(By.XPATH,"//span[text()='城市']")
        self.city2=(By.XPATH,"//li[text()='唐山市']")
        self.village=(By.XPATH,"//span[text()='区/县']")
        self.village2=(By.XPATH,"//li[text()='路北区']")
        self.address=(By.XPATH,"//*[@name='address']")
        self.mean=(By.XPATH,"//span[text()='现金支付']")
        self.realbtn=(By.XPATH,"//*[@class='go-btn-wrap']/button/span")

    def add_address(self):
        self.pyselenium.click(self.add_address_btn)
        self.pyselenium.switch_to_frame(self.iframe)

    def new_address(self,name,alias,tel,address):
        self.pyselenium.send_keys(self.name,name)
        self.pyselenium.send_keys(self.alias,alias)
        self.pyselenium.send_keys(self.tel,tel)
        self.pyselenium.click(self.arae)
        self.pyselenium.click(self.arae2)
        self.pyselenium.click(self.city)
        self.pyselenium.click(self.city2)
        self.pyselenium.click(self.village)
        self.pyselenium.click(self.village2)
        self.pyselenium.send_keys(self.address,address)
        self.pyselenium.click((By.XPATH,"//span[text()='保存']"))
        
    def pay(self):
        self.pyselenium.switch_to_default_content()
        self.pyselenium.click(self.mean)
        self.pyselenium.click(self.realbtn)