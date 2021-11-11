# -*- coding:utf-8 -*-

from base.basepage import FindElement


class Adolescent_Model:
    """
    青少年模式
    """
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)
