
class NewSlide():
    """
    滑动屏幕的方法
    使用方法   输入毫秒  代表滑动多长时间
    """
    def __init__(self, driver):
        self.driver = driver
    def get_size(self):#获取屏幕长宽高
        # 打印屏幕高和宽
        # print(self.driver.get_window_size())
        # 获取屏幕的高
        x = self.driver.get_window_size()['width']
        # 获取屏幕宽
        y = self.driver.get_window_size()['height']
        return (x,y)
    def swipe_left(self,t):#向左滑动
        screen = self.get_size()
        x = screen[0]
        y = screen[1]
        x1 = int(x * 0.9)
        y1 = int(y * 0.5)
        x2 = int(x * 0.1)
        y2 = int(y * 0.5)
        self.driver.swipe(x1,y1,x2,y2,t)
    def swipe_right(self,t):#向右滑动
        screen = self.get_size()
        x = screen[0]
        y = screen[1]
        x1 = int(x * 0.1)
        y1 = int(y * 0.5)
        x2 = int(x * 0.9)
        y2 = int(y * 0.5)
        self.driver.swipe(x1, y1, x2, y2, t)

    def swipeUp(self, t):
        """向上屏幕滑动"""
        screen = self.get_size()
        x = screen[0]
        y = screen[1]
        x1 = int(x * 0.5)
        y1 = int(y * 0.25)
        x2 = int(x * 0.5)
        y2 = int(y * 0.75)
        self.driver.swipe(x1, y1, x2, y2, t)



    def swipeDown(self, t):
        """向下屏幕滑动"""

        screen = self.get_size()
        x = screen[0]
        y = screen[1]
        x1 = int(x * 0.5)
        y1 = int(y * 0.75)
        x2 = int(x * 0.5)
        y2 = int(y * 0.25)
        self.driver.swipe(x1, y1, x2, y2, t)