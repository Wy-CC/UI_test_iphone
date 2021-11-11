import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.seek import Seek
from page.fristhome import HomePage
from page.tobing import ToBing


class TestToBing(unittest.TestCase):
    """即将上线"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.seekobj = Seek(ios_driver)
        self.homeobj = HomePage(ios_driver)
        self.tbobj = ToBing(ios_driver)


    def test_1(self):
        """
        即将上线 预约影片
        :return:
        """
        time.sleep(2)
        self.homeobj.becoming_button().click()
        self.tbobj.tobetitle_button()
        print("进入即将上线页面")
        self.tbobj.details_button().click()
        print("进入影片详情")
        self.tbobj.remind_button().click()
        print("点击预约")
        self.tbobj.order_button()
        print("预约影片成功")

    def test_2(self):
        """
        即将上线 取消预约
        :return:
        """
        time.sleep(2)
        self.homeobj.becoming_button().click()
        self.tbobj.tobetitle_button()
        print("进入即将上线页面")
        self.tbobj.details_button().click()
        print("进入影片详情")

        self.tbobj.order_button().click()
        print("取消预约")
        self.tbobj.remind_button()
        print("取消预约成功")




    def tearDown(self):
        self.tbobj.driver.close_app()