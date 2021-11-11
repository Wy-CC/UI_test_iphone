from  base.basepage import FindElement
class ToBing:
    """
    即将上线页面
    """
    def __init__(self,driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 即将上线title 按钮
    def tobetitle_button(self):
        return self.find.get_element('ToBing', 'tobetitle')
    #已预约
    def order_button(self):
        return self.find.get_element('ToBing', 'order')
    #详情
    def details_button(self):
        return self.find.get_element('ToBing', 'details')
    #提醒我
    def remind_button(self):
        return self.find.get_element('ToBing', 'remind')