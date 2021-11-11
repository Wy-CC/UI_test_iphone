# # -*- coding:utf-8 -*-
import time
import unittest
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.home_Drplay import Home_Drplay
from page.movie_detail import Movie_Detail


class TestHdrplay(unittest.TestCase):
    """首页每日推荐"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.home = HomePage(ios_driver)
        self.homedr = Home_Drplay(ios_driver)
        self.detalis = Movie_Detail(ios_driver)

    def test_drplay_home(self):
        """
        首页每日推荐--首页直接播放用例
        :return:
        """
        # time.sleep(5)
        self.homedr.mute_button().click()  # 开启小视频声音
        self.homedr.moviecollect_button().click()  # 加入片单
        self.home.play_button().click()  # 点击首页-每日推荐-播放按钮

    def test_drplay_details(self):
        """
        首页每日推荐--详情页播放用例
        ：return：
        """
        # time.sleep(5)
        self.homedr.details_button().click()  # 进每日推荐详情
        self.detalis.play().click()  # 详情页点播放按钮
