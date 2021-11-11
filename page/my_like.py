from  base.basepage import FindElement
class MyLike:
    """
    喜欢影视页面
    """
    def __init__(self,driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 喜欢影视返回 按钮
    def like_back_button(self):
        return self.find.get_element('MyLike', 'like_back')
    #喜欢影视页面title
    def like_title_button(self):
        return self.find.get_element('MyLike', 'like_title')
    #影片名字  一拳超人
    def decide_movie_button(self):
        return self.find.get_element('MyLike', 'decide_movie')