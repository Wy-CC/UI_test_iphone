#coding=utf-8

from base.basepage import FindElement
class Little_Video:

    """
    小视频播放页

    """
    def __init__(self,driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 关闭
    def video_close(self):
        return self.find.get_element('little_video','video_close')

    def video_play(self):
        return self.find.get_element('little_video', 'video_play')

    def add_coollect(self):
        return self.find.get_element('little_video', 'add_coollect')

    def click_detail(self):
        return self.find.get_element('little_video', 'click_detail')



