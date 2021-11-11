import unittest
import time
from appium import webdriver

from config.wddriver import desired_caps
from page.login import Dmo
# from pageobjects.shouye import Shouye



#登录
# @ddt
class TestLogin(unittest.TestCase):
    """登录模块"""

    def setUp(self):

        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.loginobj = Dmo(ios_driver)
        # self.shouyeobj = Shouye(ios_driver)






    def test_1(self):
        """
        登录用例
        :return:
        """

        time.sleep(5)
        self.loginobj.newlogin_button().click()#点击登录注册按钮
        time.sleep(3)

        self.loginobj.phonenum_button().send_keys('10000000006')#输入1 1
        self.loginobj.yanzhengma_button().click()#获取验证码
        self.loginobj.shuru_button().send_keys('0669')
        # self.loginobj.qingchu_button().click()#点击手机号输入框 x
        # self.loginobj.phonenum_button().send_keys(1)  # 输入1
        # self.loginobj.yanzhengma_button().click()  # 获取验证码
        # self.loginobj.qingchu_button().click()  # 点击手机号输入框 x
        # self.loginobj.phonenum_button().send_keys(10000000006)  # 输入10000000006
        # self.loginobj.yanzhengma_button().click()  # 获取验证码
        # self.loginobj.shuru_button().send_keys(222)#输入错误的验证码
        # self.loginobj.qingchu_button().click()  # 清除错误的验证码
        # time.sleep(2)
        #
        # self.loginobj.shuru_button().send_keys('2 2')  # 输入错误的验证码
        # self.loginobj.qingchu_button().click()  # 清除错误的验证码
        # time.sleep(2)
        # self.loginobj.shuru_button().send_keys('0669')#输入正确的验证码
        # print('登录成功')
        # time.sleep(10)
        # self.shouyeobj.shouye_button()  # 首页首页键显示
        # self.shouyeobj.sousuo_button()  # 首页搜索展示
        # self.shouyeobj.jingcai_button()  # 首页精彩展示
        # self.shouyeobj.yingping_button()  # 首页影评展示
        # self.shouyeobj.gengduo_button()  # 首页更多展示





    def tearDown(self):
        self.loginobj.driver.close_app()