import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.seek import Seek
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail


class TestSeek(unittest.TestCase):
    """搜索"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.seekobj = Seek(ios_driver)
        self.homeobj = HomePage(ios_driver)
        self.mvobj = Movie_Detail(ios_driver)

    # 搜索框搜索电视剧季度剧电影
    def test_1(self):
        """
        进入搜索页面执行搜索用例
        :return:
        """
        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳超人')  #输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  #点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button() #点击搜索结果
        self.mvobj.yqcrtitle_button()  #判断是否搜索正确
        self.mvobj.close_button().click() #关闭影片详情
        self.seekobj.seekclera_button().click() #清空搜索框内容


        self.seekobj.seek_button().send_keys('白鹿原')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.blytitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click() #清空搜索框内容

        self.seekobj.seek_button().send_keys('斯巴达克斯')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.sbdkstitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click() #清空搜索框内容

    # 搜索框输入影片首字母
    def test_2(self):
        """
        搜索框输入影片首字母
        :return:
        """

        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('yqcr')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.yqcrtitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click()  # 清空搜索框内容

        self.seekobj.seek_button().send_keys('bly')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.blytitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click()  # 清空搜索框内容

        self.seekobj.seek_button().send_keys('sbdks')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.sbdkstitle_button()  # 判断是否搜索正确


    # 搜索部分关键字
    def test_3(self):
        """
        搜索部分关键字
        :return:
        """
        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.yqcrtitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click()  # 清空搜索框内容

        self.seekobj.seek_button().send_keys('白鹿')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.blytitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click()  # 清空搜索框内容

        self.seekobj.seek_button().send_keys('达克斯')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.fristseekmovie_button()  # 点击搜索结果
        self.mvobj.sbdkstitle_button()  # 判断是否搜索正确
        self.mvobj.close_button().click()  # 关闭影片详情
        self.seekobj.seekclera_button().click()  # 清空搜索框内容




    def test_4(self):
        """
        点我求片
        :return:
        """
        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('青云志')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.clickmeseekmovie_button().click()#点击点我求片

    def test_5(self):
        """
        点我反馈
        :return:
        """
        time.sleep(2)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('白鹿原')  # 输入搜索词
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()  # 点击键盘搜索按钮
        time.sleep(2)
        self.seekobj.clickmetalk_button().click()#点击点我反馈
        self.seekobj.talksucceed_button()  #点击成功 敬请期待

    def tearDown(self):
        self.seekobj.driver.close_app()






