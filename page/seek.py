from base.basepage import FindElement
class Seek:
    """搜索页面"""
    def __init__(self,driver):
        self.driver = driver
        self.adc = FindElement(driver)

    #搜索输入条 x键
    def seekclera_button(self):
        return self.adc.get_element('SeekPage','seekclera')

    # 搜索输入框
    def seek_button(self):
        return self.adc.get_element('SeekPage','seek')

    # 手机键盘确定按钮
    def iphoneseek_button(self):
        return self.adc.get_element('SeekPage','iphoneseek')

    # 搜索 取消按钮
    def cancel_button(self):
        return self.adc.get_element('SeekPage','cancel')
    #点我求片
    def clickmeseekmovie_button(self):
        return self.adc.get_element('SeekPage','clickmeseekmovie')

    # 热门搜索排行榜第一个影片的图片
    def hotfirstmovie_button(self):
        return self.adc.get_element('SeekPage','hotfirstmovie')
    #热门搜索排行榜第一个影片的播放按钮
    def hotfirstmovieplay_button(self):
        return self.adc.get_element('SeekPage','hotfirstmovieplay')

    # 搜索出来第一个影片的按钮
    def fristseekmovie_button(self):
        self.driver.tap([(62,140)])

    # 点我反馈
    def clickmetalk_button(self):
        return self.adc.get_element('SeekPage', 'clickmetalk')
    #敬请期待
    def talksucceed_button(self):
        return self.adc.get_element('SeekPage', 'talksucceed')

    # 搜索出来的第一个影片
    def first_movie(self):
        return self.adc.get_element('SeekPage', 'first_movie')