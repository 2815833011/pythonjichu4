

from src.po.login_page import LoginPage


class TestLoging:
    def test_lgoin(self):
        loginpage=LoginPage()
        loginpage.navigets()
        loginpage.login("tangying",123456,"A1B2")
        loginpage.whether("登录成功")

        