import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from config.newslide import NewSlide


from page.fristhome import HomePage
from page.wonderful import Wonderful
from page.movie_detail import Movie_Detail
from page.movie_player import Movie_Player


class Test_Wonderful(unittest.TestCase):
    """
    精彩导视
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.home = HomePage(ios_driver)
        self.wonderfulobj = Wonderful(ios_driver)
        self.detailobj = Movie_Detail(ios_driver)
        self.nlobj = NewSlide(ios_driver)
        self.mpobj = Movie_Player(ios_driver)

    def test_1(self):
        """
       精彩导视滑动 加入片单 进入详情
        """

        time.sleep(2)
        self.home.two_button()
        self.wonderfulobj.jion_name()
        self.wonderfulobj.play_name()
        self.wonderfulobj.deteil_name()
        time.sleep(2)
        self.nlobj.swipe_left(20000)#滑动到下一个视频.
        print("滑动到下一个视频")
        self.wonderfulobj.jion_name()
        self.wonderfulobj.play_name()
        self.wonderfulobj.deteil_name()
        time.sleep(2)
        self.nlobj.swipe_right(20000)
        print("滑动到上一个视频")
        self.wonderfulobj.jion_name().click()
        print("加入片单")
        self.wonderfulobj.play_name()
        self.wonderfulobj.deteil_name().click()
        print("进入影片详情")
        time.sleep(3)
        self.detailobj.joincoollect()
        self.detailobj.share_button()
        self.detailobj.download_button()

    def test_2(self):
        """
       精彩导视影片播放
        """

        time.sleep(2)
        self.home.two_button()
        self.wonderfulobj.jion_name()
        self.wonderfulobj.play_name()
        self.wonderfulobj.deteil_name()
        self.wonderfulobj.play_name().click()
        print("播放精彩导视影片")
        time.sleep(15)
        self.mpobj.centre_button()
        self.mpobj.return_button().click()

    def tearDown(self):
        self.detailobj.driver.close_app()

