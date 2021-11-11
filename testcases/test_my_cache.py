import unittest
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_down import My_Down
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.seek import Seek
from page.video import Video
import time

class Test_My_Cache(unittest.TestCase):
    """
    我的缓存
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.homeobj = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.mvobj = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)
        self.seekobj = Seek(ios_driver)
        self.mydown = My_Down(ios_driver)

    def test_1(self):
        """
        我的缓存
        """
        print('搜索内容 进入详情页')
        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('erz\n')  # 输入搜索词
        time.sleep(2)
        self.seekobj.first_movie().click()  # 点击搜索结果

        print('点击下载进行缓存')
        self.mvobj.download().click()

        print('清晰度 选择选择标清')
        # self.mvobj.high().click()
        self.mvobj.standard().click()

        """
        电视剧时执行
        """
        # print('选择第一位 进行缓存')
        # self.mvobj.first_down().click()
        # print('查看我的缓存')
        # self.mvobj.my_down().click()
        # print('缓存页 第一位：'+self.mydown.donwload_name())

        """
        电影时执行
        """
        print('查看我的缓存')
        self.mvobj.my_down().click()
        print('缓存页 第一位：'+self.mydown.donwload_name())

        print('点击编辑')
        self.mydown.donw_edit().click()

        print('点击全选 选中所有影片')
        self.mydown.select_all().click()

        print('点击取消全选 取消选中所有影片')
        self.mydown.unselect_all().click()

        print('手动选中任意影片')
        self.mydown.first_movie_click().click()

        print('选中的影片是：'+self.mydown.first_movie_name())

        print('点击删除 弹起二次确认弹窗')
        self.mydown.delete().click()

        print('点击取消 弹窗消失')
        self.mydown.cancel().click()

        print('再次点击删除 选择确认')
        self.mydown.delete().click()
        self.mydown.continue1().click()

        print('删除后的列表第一位名称：'+self.mydown.first_movie_name())


        print('回到首页')
        self.mydown.donwliad_back().click()
        # self.mvobj.down_close().click()
        self.mvobj.close_button().click()  # 关闭影片详情

    def test_2(self):

        print('进入个人页')
        self.homeobj.my_home().click()
        self.myhome.cache().click()
        print('查看我的缓存第一位:'+self.mydown.last_movie_name())

        print('点击已缓存电影 进入播放器')
        self.mydown.donwload_click2().click()
        self.mydown.first_movie1().click()

        print('暂停 / 开始 / 标题 / 进度条 / 清晰度 / 全屏控件展示正常')

        # print('返回个人页，返回首页 点击搜索')
        #
        # print('搜索内容 进入详情页')
        #
        # print('点击下载进行缓存，校验提示无法缓存')

        print('播放器内返回')
        time.sleep(5)
        self.play.click_movie().click()
        print('电影名称：'+self.play.movie_name())
        self.play.movie_back().click()

        print('返回到个人中心')
        self.mydown.donwliad_back().click()



















