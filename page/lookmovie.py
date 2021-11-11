from base.basepage import FindElement


class LookMovie:
    """
    继续观看页面
    """
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 返回键
    def onelogin_button(self):
        return self.find.get_element('LookMovie', 'lookmovieback')
    #继续观看 标题
    def seemoviestitle_button(self):
        return self.find.get_element('LookMovie', 'seemoviestitle')
    #清空按钮
    def empty_button(self):
        return self.find.get_element('LookMovie', 'empty')
    #提示
    def emptyhint_button(self):
        return self.find.get_element('LookMovie', 'emptyhint')
    #确定
    def emptyyes_button(self):
        return self.find.get_element('LookMovie', 'emptyyes')
    #取消
    def emptyno_button(self):
        return self.find.get_element('LookMovie', 'emptyno')
    #继续观看列表第一位 影片
    def movielist_button(self):
        return self.find.get_element('LookMovie', 'movielist')

    # 继续观看列表第一位 影片 观影时长
    def movielisttime_button(self):
        return self.find.get_element('LookMovie', 'movielisttime')
