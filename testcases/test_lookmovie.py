import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from config.newslide import NewSlide

from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video
from page.my_like import MyLike
from page.seek import Seek
from page.lookmovie import LookMovie
from page.movie_player import Movie_Player


class Test_Lookmovie(unittest.TestCase):
    """
    继续观看
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)
        self.mylikeobj = MyLike(ios_driver)
        self.homeobj = HomePage(ios_driver)
        self.seekobj = Seek(ios_driver)
        self.lookmovieobj = LookMovie(ios_driver)
        self.nlobj= NewSlide(ios_driver)
        self.mpobj= Movie_Player(ios_driver)

    def test_1(self):
        """
        进入继续观看 播放影片
        """

        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳超人')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.detail.play().click()
        time.sleep(15)
        self.mpobj.centre_button()
        self.mpobj.return_button().click()


    def test_2(self):
        """
        进入继续观看 播放影片
        """

        time.sleep(2)
        self.nlobj.swipeDown(30000)
        self.homeobj.golook_button().click()
        movie = self.lookmovieobj.movielist_button().text
        oldtime = self.lookmovieobj.movielisttime_button().text
        print(f"继续观看影片名称{movie}和时间{oldtime}")
        self.lookmovieobj.movielist_button().click()
        self.detail.play().click()
        time.sleep(15)
        self.mpobj.centre_button()
        self.mpobj.return_button().click()

        # self.detail.close_button().click()
        # newtime = self.lookmovieobj.movielisttime_button().text
        # print(f"继续观看新的时间{newtime}")



    def test_3(self):
        """
        进入继续观看 续播成功
        """

        time.sleep(2)
        self.home.my_home().click()
        self.myhome.keeplook_button().click()
        movie = self.lookmovieobj.movielist_button().text
        oldtime = self.lookmovieobj.movielisttime_button().text
        print(f"继续观看续播影片名称{movie}和时间{oldtime}")


    def tearDown(self):
        self.mpobj.driver.close_app()