from base.basepage import FindElement



class Wonderful:
    '''
    精彩导视页面
    '''

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 精彩导视关闭按钮
    def wonderfulclose_name(self):
        return self.find.get_element('Wonderful', 'wonderfulclose')
    #播放
    def play_name(self):
        return self.find.get_element('Wonderful', 'play')
    #加入片单
    def jion_name(self):
        return self.find.get_element('Wonderful', 'jion')
    #详情
    def deteil_name(self):
        return self.find.get_element('Wonderful', 'deteil')
    #继续播放
    def goplay_name(self):
        return self.find.get_element('Wonderful', 'goplay')