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
from page.my_like import MyLike
from page.seek import Seek


class Test_My_Like(unittest.TestCase):
    """
    喜欢影视
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
        self.seekobj = Seek(ios_driver)

    def test_1(self):
        """
        将影片变为喜欢影片
        """
        time.sleep(2)
        self.home.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳超人')  #输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  #点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button() #点击搜索结果
        self.detail.evaluate_button().click()
        self.detail.praisse_button().click()
        self.detail.close_button().click()
        self.home.firstpage_button().click()
        self.home.my_home().click()
        self.myhome.likemovie_button().click()
        self.mylikeobj.like_title_button()
        name=self.mylikeobj.decide_movie_button().text
        print(111,name)
        if name=="一拳超人":
            print("影片 一拳超人已经加到喜欢影视")
        else:print('失败')


    def test_2(self):
        """
        删除喜欢影片
        """
        time.sleep(2)
        self.home.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳超人')  #输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  #点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button() #点击搜索结果
        self.detail.like_button().click()
        self.detail.close_button().click()
        self.home.firstpage_button().click()
        self.home.my_home().click()
        self.myhome.likemovie_button().click()
        self.mylikeobj.like_title_button()

        if self.mylikeobj.decide_movie_button():
            print("影片 一拳超人 喜欢影视列表删除失败")
        else:
            print("影片 一拳超人 喜欢影视列表删除成功")


    def tearDown(self):
        self.mylikeobj.driver.close_app()



