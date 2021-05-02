#  coding: utf-8
from script.module import *
import time
import os.path
import unittest
import HTMLTestRunner
class MQCTest(unittest.TestCase):
    def setUp(self):
        # 初始化测试环境
        pass

    def testLogin(self):
        # 测试主体
        tspath = os.path.abspath('.')
        tsname= tspath+'\\data\\testsuite.xlsx'
        self.assertTrue(read_testsuite(tsname))

    def tearDown(self):
        # 收尾部分
        pass

if  __name__  ==  "__main__":
    #  unittest.main()
    test = unittest.TestSuite()
    test.addTest(MQCTest("testLogin"))
    rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    file_path = os.path.abspath('.')+'\\report\\'+rq+'-result.html'
    file_result = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'MQCTour测试报告',description=u'用例执行情况')
    runner.run(test)
    file_result.close()
