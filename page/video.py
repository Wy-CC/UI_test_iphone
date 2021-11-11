# coding=utf-8

from base.basepage import FindElement



class Video:

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 电影名称
    def movie_name(self):
        return self.find.get_element('Play', 'play_movie_name').text

    # 全屏播放页面 返回按钮
    def movie_back(self):
        return self.find.get_element('Play', 'close')

    # 全屏播放页面 点击屏幕
    def click_movie(self):
        return self.find.get_element('Play', 'click_movie')











