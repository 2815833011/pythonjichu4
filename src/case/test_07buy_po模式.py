
import pytest
from src.util.pyselenium import Pyselenium
from src.po.index_page import IndexPage
from src.po.shopinto_page import ShopInto
from src.po.shoppay_page import ShopPay
import time
class TestBuy:
    def setup_class(self):
        self.pyselenium=Pyselenium()
        self.index_page=IndexPage(self.pyselenium)
        self.shopinto_page=ShopInto(self.pyselenium)
        self.shoppay_page=ShopPay(self.pyselenium)

    def teardown_method(self):
        self.pyselenium.delete_all_cookies()
        self.pyselenium.refresh()

    @pytest.mark.usefixtures("login_fixpom")
    def test_buy(self):
        self.index_page.click_tobuy()
        self.pyselenium.switch_to_new_window()
        self.shopinto_page.click_tobuy()
        self.shoppay_page.add_address()
        self.shoppay_page.new_address("tangying","tangying","17673415861","sdfesdfehs")
        time.sleep(5)
        self.shoppay_page.pay()
        time.sleep(5)
        
    