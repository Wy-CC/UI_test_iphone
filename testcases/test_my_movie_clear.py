
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

    def test_1(self):
        """
        我的片单具体执行用例
        """

        time.sleep(2)
        print('进入个人页')
        self.home.my_home().click()

        print('个人页点击我的片单')
        self.myhome.coollect_button().click()

        print('点击清除按钮')
        try:
            self.mycoollect.clear().click()
            print('二级弹窗点击确认')
            self.mycoollect.isclear().click()

            print('清除校验')
            is_show = self.mycoollect.no_list()

            if not is_show:
                print('空页面展位图展示了')
        except AttributeError:
            print('没内容 不展示清除按钮')
            self.myhome.back().click()
            self.myhome.back().click()
            time.sleep(2)
            print('点击首页每日推荐点击添加 片单')
            self.home.moviecollect_button().click()
            self.test_1()


