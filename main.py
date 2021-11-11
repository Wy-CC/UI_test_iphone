import os
import unittest
import time
import yagmail
# from common.HTMLTestRunner import HTMLTestRunner


# 引入测试模块
from testcases import test_login
from testcases import test_video
from testcases import test_seek
from testcases import test_my_like
from testcases import test_lookmovie
from testcases import test_homeclass
from testcases import test_Wonderful
from testcases import test_tobing




# 创建测试集

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# 添加测试用例到测试集

# suite.addTests(loader.loadTestsFromModule(test_login))  # 登录页面测试用例
# suite.addTests(loader.loadTestsFromModule(test_video))  # 放映厅测试用例
# suite.addTests(loader.loadTestsFromModule(test_seek))  # 搜索用例
# suite.addTests(loader.loadTestsFromModule(test_my_like))  # 喜欢影视用例
# suite.addTests(loader.loadTestsFromModule(test_lookmovie))  # 喜欢影视用例
# suite.addTests(loader.loadTestsFromModule(test_homeclass))  # 首页分类用例
# suite.addTests(loader.loadTestsFromModule(test_Wonderful))  # 精彩导视用例
suite.addTests(loader.loadTestsFromModule(test_tobing))  # 精彩导视用例



# 执行测试用例 （调试展示）
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)

# now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
# report_html = "./report/" + now_time + "result.html"
# fp = open(report_html, "wb")
#
# runner = HTMLTestRunner(
#     stream = fp,
#     verbosity=2,
#     title="南瓜电影ui测试",
#     description="环境：正式环境 , version：5.2.2 ,机型：苹果6sp，系统：14。4"
#     )
# runner.run(suite)
# fp.close()
