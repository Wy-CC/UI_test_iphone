# coding=utf-8

from base.basepage import FindElement

"""
个人页
"""


class Finmreview_Detail:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 影评详情

    def fd_input(self):
        return self.find.get_element('Fimreview_Detail', 'input')

    def fd_back(self):
        return self.find.get_element('Fimreview_Detail', 'back')

    def fd_comment(self):
        return self.find.get_element('Fimreview_Detail', 'comment')

