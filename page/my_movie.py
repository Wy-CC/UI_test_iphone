# coding=utf-8

from base.basepage import FindElement


class My_Movie:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 精彩推荐详情页添加我的片单
    def newlogin_button(self):
        return self.find.get_element('LoginElement', 'newlogin')


