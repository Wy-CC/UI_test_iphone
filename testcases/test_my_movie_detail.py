
import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.little_video import Little_Video
from page.login import Dmo
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video


class Test_My_Movie_Detail(unittest.TestCase):
    """
    我的片单 详情页
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)
        self.litvideo = Little_Video(ios_driver)
        self.loginobj = Dmo(ios_driver)
        self.mvdetail = Movie_Detail(ios_driver)

    def isok(self,moviename,movename,a):

        if a == 0:
            if moviename != movename:
                print('信息不同 返回个人页 再次获取')
                time.sleep(2)
                self.myhome.back().click()
                self.myhome.back().click()
                self.case1(0)
            else:
                print('信息相同，校验正确返回个人页')
                self.myhome.back().click()
                self.myhome.back().click()
        else:
            if moviename != movename:
                print('信息不相同，确认已移除')
                self.myhome.back().click()
                self.myhome.back().click()

    def case1(self,a=0):
        """
        我的片单具体执行用例
        """
        time.sleep(2)
        print('点击每日推荐详情 进入详情页')
        self.home.details_button().click()

        print('点击加入片单')
        time.sleep(5)

        self.mvdetail.joincoollect().click()
        print('点击播放 进入播放器获取影片信息')
        self.mvdetail.play().click()
        time.sleep(5)
        self.play.click_movie().click()

        moviename = self.play.movie_name()
        print('添加的影片信息:' + moviename)
        time.sleep(0.5)
        self.play.movie_back().click()
        time.sleep(1)
        print('到我的片单页查看已加入片单')
        self.mvdetail.detail_close().click()

        print('进入个人页')
        self.home.my_home().click()

        print('个人页点击我的片单')
        self.myhome.coollect_button().click()

        movename = self.mycoollect.first_move_name()
        moveother = self.mycoollect.first_move_other()
        print('片单页第一位影片：' + movename + " - " + moveother)
        self.isok(movename, moviename, a)

    def test_1(self):

        self.case1(0)
        print('再次进入详情页 移除片单')
        self.case1(1)


