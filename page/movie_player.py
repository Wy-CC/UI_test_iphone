# coding=utf-8
import time
from base.basepage import FindElement
from appium.webdriver.common.touch_action import TouchAction


class Movie_Player:
    def __init__(self, driver):
        self.driver = driver
        self.adc = FindElement(driver)

    def movie_name(self):
        return self.adc.get_element('MoviePlay', 'movie_name')

    # 播放器内--唤起操作栏
    def arouse_button(self):
        return self.adc.get_element('MoviePlay', 'screen')

    # 播放器内--左上角返回
    def return_button(self):
        return self.adc.get_element('MoviePlay', 'return')

    # 播放器内--极享jsharer
    def jsharer_button(self):
        return self.adc.get_element('MoviePlay', 'jsharer')

    # 播放器内极享--立即体验
    def experience_button(self):
        return self.adc.get_element('MoviePlay', 'experience')

    # 点击升级会员
    def upgrade_button(self):
        return self.adc.get_element('MoviePlay', 'upgrade')

    # 个人中心页--返回
    def goback_button(self):
        return self.adc.get_element('MyMore', 'goback')

    # 播放器内--画中画
    def PinP_button(self):
        return self.adc.get_element('MoviePlay', 'pinp')

    # 播放器内--暂停/开始
    def throughout_button(self):
        return self.adc.get_element('MoviePlay', 'throughout')

    # 锁屏
    def lock_button(self):
        return self.adc.get_element('MoviePlay', 'lock')

    # 开锁
    def unlock_button(self):
        return self.adc.get_element('MoviePlay', 'unlock')

    # 清晰度
    def ultra_button(self):
        return self.adc.get_element('MoviePlay', 'ultra')

    # 标清
    def standard_button(self):
        return self.adc.get_element('MoviePlay', 'standard')

    # 字幕
    def subtitle_button(self):
        return self.adc.get_element('MoviePlay', 'subtitle')

    # 中文字幕
    def chinese_button(self):
        return self.adc.get_element('MoviePlay', 'chinese')

    # 英文字幕
    def english_button(self):
        return self.adc.get_element('MoviePlay', 'english')

    # 倍速
    def speed_button(self):
        return self.adc.get_element('MoviePlay', 'speed')

    # 2倍速
    def tspeed_button(self):
        return self.adc.get_element('MoviePlay', 'two_speed')

    # 1.5倍速
    def opspeed_button(self):
        return self.adc.get_element('MoviePlay', 'opf_speed')

    # 1倍速
    def onspeed_button(self):
        return self.adc.get_element('MoviePlay', 'one_speed')

    # 点击屏幕中心
    def centre_button(self):  # 点击播放页 中心的坐标 （唤起进度条 影片名称等弹框）
        self.driver.tap([(306, 160)])

    # 快进
    def speed1_button(self):
        return self.adc.get_element('MoviePlay', 'speed1')

    # 快退
    def fast_button(self):
        return self.adc.get_element('MoviePlay', 'fast')