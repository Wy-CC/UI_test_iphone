import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.videotab import Video_hall



class TestVideoHall(unittest.TestCase):
    """放映厅"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = Video_hall(ios_driver)

    def test_1(self):
        """
        点击底tab 进入放映厅
        :return:
        """

        time.sleep(2)
        # 点击放映厅Tab
        self.videohall.video_tab_button().click()
        time.sleep(1.5)

        # 点击热闹 / 最新tab
        self.videohall.hot_tab().click()
        time.sleep(0.5)
        self.videohall.new_tab().click()

        print('点击热闹 / 最新tab')

        # 创建放映厅
        self.videohall.create_live_button().click()
        time.sleep(0.5)
        self.videohall.replace_list_one().click()
        self.videohall.close_live().click()

        # 随机进入放映厅
        self.videohall.random_tab().click()
        self.videohall.close_live().click()

        print('随机进入放映厅后返回')

        # 点击我的厅 / 我的资产页面展示 / 近期动态页面展示 /创建历史页面展示
        self.videohall.my_live_tab().click()
        """
        前置条件 需要保证账号内一定有资产 / 创建历史 / 近期动态记录
        进入页面后 判断资产数不为空 / 近期动态列表 / 创建历史页 第一位是否有内容
        """
        # 获取到钱数 不等于0
        money = self.videohall.my_money().text
        print('金额：'+money)
        assert money != "0"

        print('进入我的厅')

        # 近期历史记录
        self.videohall.news_list()
        time.sleep(1)
        print('检查近期历史记录')

        # 点击创建历史
        self.videohall.mylive_history().click()
        print('进入创建历史')

        # 创建历史列表
        self.videohall.myLive_history_list()

        # 创建历史点击返回
        self.videohall.mylive_history_back().click()
        print('创建历史返回')

        # 放映厅发布弹幕
        self.videohall.click_list_one().click()
        time.sleep(1.5)
        self.videohall.comment().send_keys('大噶好～')
        self.videohall.comment().send_keys('\n')

        # 放映厅发送礼物
        self.videohall.gift().click()
        seed_namber = self.videohall.seed_number().text
        print('南瓜籽数'+seed_namber)
        print("送出的礼物："+self.videohall.gift_name())
        self.videohall.gift_list_one().click()
        print("消费南瓜籽：" + self.videohall.gift_name())
        self.videohall.send_gift().click()

        # 更换影片
        self.videohall.more().click()
        self.videohall.replace().click()
        time.sleep(1)
        self.videohall.replace_list_one().click()

        # 全屏模式下操作
        self.videohall.click_move().click()
        # self.videohall.click_move().click()
        self.videohall.fullScreen_click().click()

        time.sleep(2)
        self.videohall.fullscreen_move().click()
        self.videohall.fullScreen_comment().click()
        self.videohall.fullScreen_comment1().send_keys('大噶好～')
        self.videohall.fullScreen_comment_send().click()

        time.sleep(1)
        self.videohall.fullscreen_move().click()
        self.videohall.fullscreen_move().click()
        self.videohall.fullscreen_back().click()




        # # 点击搜索按钮
        # self.videohall.search_button().click()

    # def tearDown(self):
    #     self.loginobj.driver.close_app()
