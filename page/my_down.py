# coding=utf-8

from base.basepage import FindElement


class My_Down:
    """
    我的缓存
    """
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 下载中电影的名字
    def donwload_name(self):
        return self.find.get_element('My_download', 'donwload_name').text

    # 返回
    def donwliad_back(self):
        return self.find.get_element('My_download', 'donwliad_back')

    # 点击正在缓存
    def donwload_click(self):
        return self.find.get_element('My_download', 'donwload_click')

    # 缓存页面返回
    def donw_back(self):
        return self.find.get_element('My_download', 'donw_back')

    # 缓存页面编辑
    def donw_edit(self):
        return self.find.get_element('My_download', 'donw_edit')

    # 缓存页面取消
    def cancel1(self):
        return self.find.get_element('My_download', 'cancel1')

    # 第一位电影 选中按钮
    def first_movie_click(self):
        return self.find.get_element('My_download', 'first_movie_click')

    # 第一位电影名字
    def first_movie_name(self):
        return self.find.get_element('My_download', 'first_movie_name').text

    # 全选
    def select_all(self):
        return self.find.get_element('My_download', 'select_all')

    # 取消全选
    def unselect_all(self):
        return self.find.get_element('My_download', 'unselect_all')

    # 删除
    def delete(self):
        return self.find.get_element('My_download', 'delete')

    # 继续
    def continue1(self):
        return self.find.get_element('My_download', 'continue1')

    # 取消
    def cancel(self):
        return self.find.get_element('My_download', 'cancel')

    """
    已缓存页
    """
    # 缓存页第二位
    def donwload_click2(self):
        return self.find.get_element('My_download', 'donwload_click2')

    def last_movie_name(self):
        return self.find.get_element('My_download', 'last_movie_name').text

    # 已缓存页 第一位
    def first_movie1(self):
        return self.find.get_element('My_download', 'first_movie1')


