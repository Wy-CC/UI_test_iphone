import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video


class Test_My_Movie(unittest.TestCase):
    """
    我的片单每日推荐
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)

    def test_1(self):
        """
        我的片单具体执行用例
        """
        time.sleep(2)
        print('进入详情页再返回首页 防止视频播放拿不到影片信息')
        self.home.details_button().click()
        time.sleep(1)
        self.detail.detail_close().click()

        print('点击首页每日推荐点击添加 片单')
        self.home.moviecollect_button()
        time.sleep(3)

        """
        首页的每日推荐 点击加入片单按钮，进入我的片单页面进行查看，如果信息不对称则 有可能是已经添加了 
        再次回到首页点击添加 再次进入个人页查看信息对称则 添加成功若都不对称则失败
        """
        print('点击播放 进入播放器获取影片信息')
        self.home.home_play().click()
        time.sleep(5)
        self.play.click_movie().click()
        moviename = self.play.movie_name()
        self.play.movie_back().click()

        print('添加的影片信息:' + moviename)

        print('进入个人页')
        self.home.my_home().click()

        print('个人页点击我的片单')
        self.myhome.coollect_button().click()

        movename = self.mycoollect.first_move_name()
        moveother = self.mycoollect.first_move_other()
        print('片单页第一位影片：' + movename + " - " + moveother)

        if moviename != movename:
            print('相关信息不同 返回个人页 再次获取')
            time.sleep(2)
            self.myhome.back().click()
            self.myhome.back().click()
            self.test_1()
        else:
            print('返回个人页')
            self.myhome.back().click()
