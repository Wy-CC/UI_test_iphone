# -*- coding:utf-8 -*-
import unittest
import time
from config.wddriver import desired_caps
from appium import webdriver
from page.fristhome import HomePage
from page.film_Drplay import Film_Drplay
from page.movie_detail import Movie_Detail


class TestDdrplay(unittest.TestCase):
    """剧集每日推荐"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.home = HomePage(ios_driver)
        self.film = Film_Drplay(ios_driver)
        self.detalis = Movie_Detail(ios_driver)

    def test_drplay_drama(self):
        """
        电影首页每日推荐--首页直接播放用例
        :return:
        """
        # time.sleep(5)
        self.home.movie_button().click()  # 进电影首页
        # time.sleep(5)
        self.film.mute_button().click()  # 开启小视频声音
        self.film.moviecollect_button().click()  # 加入片单
        self.home.play_button().click()  # 点击首页-每日推荐-播放按钮

    def test_drplay_details(self):
        """
        电影首页每日推荐--详情页播放用例
        ：return：
        """
        # time.sleep(5)
        self.home.movie_button().click()  # 进电影首页
        # time.sleep(5)
        self.film.details_button().click()  # 进每日推荐详情
        self.detalis.play().click()  # 详情页点播放按钮
