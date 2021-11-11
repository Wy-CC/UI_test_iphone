import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.finmreview_detail import Finmreview_Detail
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video


class Test_My_More(unittest.TestCase):
    """
    我的
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)
        self.fd = Finmreview_Detail(ios_driver)

    def test_1(self):
        """
        我的
        """
        print('首页进入个人页')
        self.home.my_home().click()

        print('我的页面点击关注')
        self.myhome.member().click()
        print('关注列表展现')
        # 拿到列表后判断列表是否为空
        self.myhome.mycheck_list

        print('关注列表第一位用户名：'+self.myhome.mycheck_list_firstname().text)
        print('点击第一位用户 进入消息页发送消息')
        self.myhome.mycheck_list_firstname().click()
        time.sleep(2)
        print('输入内容')
        self.myhome.input_click().click()
        self.myhome.input().send_keys('小南瓜顶呱呱～')
        time.sleep(1)
        self.myhome.send().click()

        print('发布的内容：'+self.myhome.chat_content())

        print('返回关注列表')
        self.myhome.chat_back().click()

        time.sleep(1)
        print('点击用户头像进入用户个人页')
        self.myhome.mycheck_list_firstimg().click()
        print('用户名：'+self.myhome.username().text)
        print('等级：'+self.myhome.level().text)
        print('关注按钮点击')
        self.myhome.follow().click()
        self.myhome.follow().click()

        print('返回关注列表')
        self.myhome.chat_back().click()

        print('点击返回 回到个人页')
        self.myhome.mycheck_back().click()

        print('我的页面点击粉丝')
        self.myhome.fans().click()

        print('粉丝页第一位用户名：'+self.myhome.my_fans_list_firstname())

        print('粉丝页点击返回 回到个人页')
        self.myhome.my_fans_back().click()

        print('我的页面点击影评')
        self.myhome.filmreview().click()

        print('影评总数：'+self.myhome.finmreview_total())
        # 如果影评为空时 不去走下面的获取影评信息，而是去添加影评
        print('第一位影评：'+self.myhome.finmreview_firsttext())

        print('点击点赞')
        self.myhome.finmreview_digg().click()
        time.sleep(1)

        print('点击评论')
        self.myhome.finmreview_comment().click()

        print('进入影评详情页')
        time.sleep(1)
        self.fd.fd_input().send_keys('小南瓜顶呱呱!!!～\n')

        print('发布的内容：'+self.fd.fd_comment().text)

        print('返回我的影评')
        self.fd.fd_back().click()

        print('影评页返回个人页')
        self.myhome.finmreview_back().click()

    def test_2(self):

        print('首页进入个人页')
        self.home.my_home().click()

        print('进入我的设置')
        self.myhome.myset().click()

        print('进入到账号与安全')
        self.myhome.account().click()

        print('进入到注销账号')
        self.myhome.cancel_account().click()

        print('注销页面信息校验')
        print(self.myhome.copyall())

        print('回到 账号与安全页')
        self.myhome.copy_back().click()

        print('返回到我的设置')
        self.myhome.peicacy_back().click()

        print('文案校验')
        print('预期：用户协议、播放修复、清除缓存、我要反馈、联系我们')
        print('实际结果：'+self.myhome.agreement()+'、'+''+self.myhome.playback()+'、'+''+self.myhome.playback()+'、'+''+self.myhome.clear()+'、'+''+self.myhome.feedback()+'、'+''+self.myhome.contact())

        print('点击登出')
        self.myhome.logout().click()
