# coding=utf-8
import configparser


class ReadIni(object):

    def read_my_ini(self,*args):

        config = configparser.ConfigParser()
        config.read('/Users/wasai/PycharmProjects/UI_test_iphone/config/findment.ini')
        # 要改成自己本地的地址
        # config.read('/Users/cuixuefei/PycharmProjects/auto_test/config/findment.ini')
        # config.read('/Users/kkkl/Downloads/UI_test_iphone/config/findment.ini')
        # config.read('/Users/cuixuefei/PycharmProjects/UI_test_iphone/config/findment.ini')

        config.read('/Users/cuixuefei/PycharmProjects/UI_test_iphone/config/findment.ini')


        # 要改成自己本地的地址
        config.read('/Users/kkkl/Downloads/UI_test_iphone/config/findment.ini')
        value = config.get(*args)
        return value

if __name__ == '__main__':
   read_init = ReadIni()
   # print(read_init.read_my_ini('LoginElement','newlogin'))