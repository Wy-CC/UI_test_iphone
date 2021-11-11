# coding=utf-8

from base.basepage import FindElement
from appium import webdriver


class Video_hall:

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 放映厅按钮
    def video_tab_button(self):
        return self.find.get_element('HomePage', 'videohall')

    # 搜索按钮
    def search_button(self):
        return self.find.get_element('videoHall', 'searchvideo')

    # 最新tab 按钮
    def new_tab(self):
        return self.find.get_element('videoHall', 'newest')

    # 热闹tab 按钮
    def hot_tab(self):
        return self.find.get_element('videoHall', 'busy')

    # 随机加入按钮
    def random_tab(self):
        return self.find.get_element('videoHall', 'randomjoin')

    # 我的厅 按钮
    def my_live_tab(self):
        return self.find.get_element('videoHall', 'mylive')

    # 创建放映厅按钮
    def create_live_button(self):
        return self.find.get_element('videoHall', 'createlive')

    # 放映厅第一个直播间
    def first_live(self):
        return self.find.get_element('videoHall', 'firstlive')

    # 我的资产
    def my_money(self):
        return self.find.get_element('videoHall', 'money')

    # 查看近期动态列表
    def news_list(self):
        if self.find.get_element('videoHall', 'list_show').is_displayed():
            print('近期动态有内容')
            return self.find.get_element('videoHall', 'list_show')
        else:
            print('近期动态无内容')
            return self.find.get_element('videoHall', 'list_none')

    # 点击返回
    def mylive_back(self):
        return self.find.get_element('videoHall', 'mylive_back')

    # 点击创建历史
    def mylive_history(self):
        return self.find.get_element('videoHall', 'mylive_history')

    # 创建历史列表检查
    def myLive_history_list(self):
        if self.find.get_element('videoHall', 'mylive_history_list').is_displayed():
            print('创建历史有内容')
            return self.find.get_element('videoHall', 'mylive_history_list')
        else:
            print('创建历史无内容')

    # 创建历史点击返回
    def mylive_history_back(self):
        return self.find.get_element('videoHall', 'mylive_history_back')

    # 放映厅内关闭按钮
    def close_live(self):
        return self.find.get_element('videoHall','close_live')

    # 点击评论框和发布评论

    def click_list_one(self):
        return self.find.get_element('videoHall','firstlive')

    def comment(self):
        return self.find.get_element('videoHall','live_comment')

    # 选择礼物
    def gift(self):
        return self.find.get_element('videoHall','gift')

    def gift_list_one(self):
        return self.find.get_element('videoHall','gift_list_one')

    def seed_number(self):
        return self.find.get_element('videoHall','seed_number')

    def send_gift(self):
        return self.find.get_element('videoHall', 'gift_send')

    def gift_name(self):
        return self.find.get_element('videoHall','gift_name').text

    # 更换影片
    def more(self):
        return self.find.get_element('videoHall','more')

    def replace(self):
        return self.find.get_element('videoHall','replace')

    def replace_list_one(self):
        return self.find.get_element('videoHall','replace_list_one')

    # 全屏

    def fullScreen_click(self):
        return self.find.get_element('videoHall', 'fullScreen_click')

    def click_move(self):
        return self.find.get_element('videoHall','click_move')

    def fullscreen_move(self):
        return self.find.get_element('videoHall','fullscreen_move')

    def fullScreen_comment(self):
        return self.find.get_element('videoHall','fullScreen_comment')

    def fullScreen_comment1(self):
        return self.find.get_element('videoHall','fullScreen_comment1')

    def fullscreen_back(self):
        return self.find.get_element('videoHall','fullscreen_back')

    def fullScreen_comment_send(self):
        return self.find.get_element('videoHall','fullScreen_comment_send')







