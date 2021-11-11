# coding=utf-8

from base.basepage import FindElement


class Film_Drplay:
    """
    电影首页每日推荐
    """

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    def home_page(self):
        return self.find.get_element('HomePage', 'drama').text

    # 每日推荐影片信息
    def recommend(self):
        return self.find.get_element('HomePage', 'recommend').text

    # 小视频静音--播放
    def mute_button(self):
        return self.find.get_element('HomePage', "mute")

    # 点击每日推荐加入片单
    def moviecollect_button(self):
        return self.find.get_element('HomePage', 'moviecollect')

    # 点击每日推荐详情
    def details_button(self):
        return self.find.get_element('HomePage', 'details')
