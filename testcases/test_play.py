import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.movie_player import Movie_Player
from page.fristhome import HomePage


# 首页每日推荐播放

class TestPlay(unittest.TestCase):
    """播放器"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.playbj = Movie_Player(ios_driver)
        self.Homebj = HomePage(ios_driver)

    def test_play(self):
        """
        播放器用例
        :return:
        """
        time.sleep(5)
        self.Homebj.play_button().click()  # 点击首页-每日推荐-播放按钮
        time.sleep(8)
        self.playbj.arouse_button().click()  # 唤起操作栏
        time.sleep(1)
        self.playbj.throughout_button().click()  # 暂停
        time.sleep(5)
        self.playbj.arouse_button().click()
        self.playbj.throughout_button().click()  # 开始
        time.sleep(5)
        self.playbj.arouse_button().click()  # 唤起操作栏
        self.playbj.lock_button().click()  # 锁屏
        # time.sleep(5)
        # self.Drplaybj.arouse_button().click()  # 唤起操作栏
        self.playbj.unlock_button().click()  # 开屏
        time.sleep(5)
        self.playbj.arouse_button().click()  # 唤起操作栏
        self.playbj.ultra_button().click()  # 点击清晰度
        time.sleep(1)
        self.playbj.standard_button().click()  # 选择标清
        time.sleep(9)
        self.playbj.arouse_button().click()  # 唤起操作栏
        self.playbj.speed_button().click()  # 点击倍速
        time.sleep(1)
        self.playbj.tspeed_button().click()  # 选择2倍速
        time.sleep(2)
        self.playbj.arouse_button().click()  # 唤起操作栏

        self.playbj.subtitle_button().click()  # 点击字幕
        self.playbj.english_button().click()  # 切换英文
        time.sleep(3)
        self.playbj.arouse_button().click()  # 唤起操作栏
        self.playbj.arouse_button().click()  # 点击极享
        self.playbj.experience_button().click()  # 点击立即体验
        time.sleep(10)
        self.playbj.arouse_button().click()  # 唤起操作栏
        self.playbj.upgrade_button().click()  # 点击升级极享
        self.playbj.goback_button().click()  # 返回首页
        # time.sleep(5)
        self.Homebj.play_button().click()  # 点击首页-每日推荐-播放按钮
