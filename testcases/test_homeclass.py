import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage


class Test_Homeclass(unittest.TestCase):
    """
    首页分类
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.home = HomePage(ios_driver)

    def test_1(self):
        """
       首页分类切换
        """

        time.sleep(2)
        self.home.episode_button()
        self.home.movie_button()
        self.home.classes_button()
        self.home.episode_button().click()
        self.home.classes_button().click()
        self.home.theaterid_button().click()
        print('切换到剧集')
        self.home.theater_button()
        print("切换到 剧集 欧美剧场分类")
        self.home.episode_button().click()
        self.home.closeclass_button().click()
        print("关闭浮层")
        self.home.episode_button()
        self.home.theater_button()
        print("关闭浮层  还是在剧集页面")


        self.home.episode_button().click()
        self.home.movie_button().click()
        print("切换到电影分类")
        self.home.movie_button()
        self.home.classes_button().click()
        self.home.warid_button().click()
        print("切换到 电影 生活情感分类")
        self.home.wartitile_button()
        self.home.movie_button().click()
        self.home.fristclass_button().click()
        print("切换到首页")
        self.home.episode_button()
        self.home.movie_button()
        self.home.classes_button()






    def tearDown(self):
        self.home.driver.close_app()