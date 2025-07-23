'''
pytest web测试报告
支持崔pytest函数的装饰
支持失败截图
环境搭建（jdk17,allure-commandline,allure-pytest） 


mac 安装allure
1. 安装 Allure
推荐使用 Homebrew 安装（如果未安装 Homebrew，点击这里安装）：

bash
brew install allure

若无法使用 Homebrew，也可以从 Allure 发布页 下载压缩包，手动解压到指定目录（例如 ~/allure-2.XX.X）。
2. 验证安装
检查 Allure 是否正确安装：

bash
allure --version

如果提示 command not found，则需要配置环境变量。
3. 配置环境变量
方法 1：自动配置（推荐）
如果使用 Homebrew 安装，通常会自动配置环境变量。若未生效，执行以下命令：

bash
echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.zshrc
source ~/.zshrc

使用方法
@allure.title("测试步骤1") 标题
allure.step("打开浏览器")   操作步骤
allure.attach(name,body,atattachment_typetach) 添加执行结果. 标题 截图内容 内容文件类型
命令行

pytest --alluredir="报告保存地址"  +"需要执行的用例"

打开测试报告
allure serve report/result

'''
import allure
from src.util.pyselenium import Pyselenium
class TestResult:
    @allure.title("测试步骤1")
    def test_01(self):
        with allure.step("打开浏览器"):
            driver=Pyselenium()

        with allure.step("打开百度") :
            driver.get("https://www.baidu.com")

        with allure.step("找到wd的元素") :
            driver.send_keys(("id","kw"),"python")
            driver.click(("id","su"))
            assert 1==2

        # with allure.step("结果截图"):
        #     allure.attach(name="执行结果",
        #                   body=driver.get_screenshot_as_png(),
        #                   attachment_type=allure.attachment_type.PNG
        #                   )

    def test_02(self):
        assert False

    def test_03(self):
        pass