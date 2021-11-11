# coding=utf-8

from base.basepage import FindElement

"""
个人页
"""


class My_Home:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 个人页我的片单
    def coollect_button(self):
        return self.find.get_element('MyMore', 'coollect')
    #个人页面 喜欢影视
    def likemovie_button(self):
        return self.find.get_element('MyMore', 'likemovie')

    # 个人页面 继续观看
    def keeplook_button(self):
        return self.find.get_element('MyMore', 'keeplook')


    # 个人页 我的缓存
    def cache(self):
        return self.find.get_element('MyMore', 'cache')


    # 返回按钮
    def back(self):
        return self.find.get_element('MyMore', 'goback')

    # 关注列表
    def member(self):
        return self.find.get_element('MyMore', 'attention')

    def mycheck_back(self):
        return self.find.get_element('Mycheck', 'mycheck_back')

    def mycheck_list(self):
        return self.find.get_element('Mycheck', 'mycheck_list')

    def mycheck_list_firstname(self):
        return self.find.get_element('Mycheck', 'mycheck_list_firstname')

    def mycheck_list_firstimg(self):
        return self.find.get_element('Mycheck', 'mycheck_list_firstimg')

    def mycheck_first_cancel(self):
        return self.find.get_element('Mycheck', 'mycheck_first_cancel')



    # 聊天页
    def input(self):
        return self.find.get_element('Chat', 'input')

    def input_click(self):
        return self.find.get_element('Chat', 'input_click')

    def send(self):
        return self.find.get_element('Chat', 'send')

    def chat_back(self):
        return self.find.get_element('Chat', 'chat_back')

    def chat_content(self):
        return self.find.get_element('Chat', 'content').text

    # 粉丝列表
    def fans(self):
        return self.find.get_element('MyMore', 'fans')

    def my_fans_back(self):
        return self.find.get_element('My_Fans', 'my_fans_back')

    def my_fans_list_firstname(self):
        return self.find.get_element('My_Fans', 'my_fans_list_firstname').text

    # 影评列表
    def filmreview(self):
        return self.find.get_element('MyMore', 'filmreview')

    def finmreview_back(self):
        return self.find.get_element('Filmreview', 'finmreview_back')

    def finmreview_total(self):
        return self.find.get_element('Filmreview', 'finmreview_total').text

    def finmreview_firsttext(self):
        return self.find.get_element('Filmreview', 'finmreview_firsttext').text

    def finmreview_digg(self):
        return self.find.get_element('Filmreview', 'finmreview_digg')

    def finmreview_comment(self):
        return self.find.get_element('Filmreview', 'finmreview_comment')

    # 我的设置
    def myset(self):
        return self.find.get_element('MyMore', 'myset')

    def account(self):
        return self.find.get_element('MyMore', 'account')

    def mysetting_back(self):
        return self.find.get_element('MyMore', 'mysetting_back')

    def agreement(self):
        return self.find.get_element('MyMore', 'agreement').text

    def playback(self):
        return self.find.get_element('MyMore', 'playback').text

    def clear(self):
        return self.find.get_element('MyMore', 'clear').text

    def feedback(self):
        return self.find.get_element('MyMore', 'feedback').text

    def contact(self):
        return self.find.get_element('MyMore', 'contact').text

    def logout(self):
        return self.find.get_element('MyMore', 'Logout')

    # 账号安全
    def account(self):
        return self.find.get_element('MyMore', 'account')

    def peicacy_back(self):
        return self.find.get_element('MyMore', 'peicacy_back')

    # 隐私设置
    def privacy_settings(self):
        return self.find.get_element('MyMore', 'privacy_settings')

    # 设备管理
    def device_management(self):
        return self.find.get_element('MyMore', 'device_management')

    # 注销账号
    def cancel_account(self):
        return self.find.get_element('MyMore', 'cancel_account')

    def copy_back(self):
        return self.find.get_element('MyMore', 'copy_back')

    def copyall(self):
        return ''+self.find.get_element('MyMore', 'copy1').text+'\n'+self.find.get_element('MyMore', 'copy2').text+'\n'+self.find.get_element('MyMore', 'copy3').text+'\n'+self.find.get_element('MyMore', 'copy4').text+'\n'+self.find.get_element('MyMore', 'copy5').text

    # 他人个人页

    def username(self):
        return self.find.get_element('Otherhome', 'username')

    def level(self):
        return self.find.get_element('Otherhome', 'level')

    def follow(self):
        return self.find.get_element('Otherhome', 'follow')

    def other_back(self):
        return self.find.get_element('Otherhome', 'back')








