from selenium import webdriver
from selenium.webdriver import ActionChains
# 加载元素隐性显示超时设置函数
from selenium.webdriver.support.wait import WebDriverWait
# 导入截图函数
from common.CapPic import CapPic
# 加载预期处理函数
from selenium.webdriver.support import expected_conditions as EC
import time
import os.path
# 导入日志处理函数
from common.LogGen import LogGen
logger = LogGen(logger='BasePage').getlog()
# 定义基础页面类文件，该类仅包含查找元素和输入数据两个函数
class BasePage(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
    #定义查找元素超时设置，当页面中某个元素在10秒内没有显示，则抛出异常，并在日志中显示
    def find_element(self,*loc):
        try:
            #loc是表示属性元组本身，*loc表示属性元组的值，EC.visibility_of_element_located需要传入两个参数
            #因此，此处智能是loc
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            #此处返回元素的属性及属性值，故使用*loc
            return self.driver.find_element(*loc)
        except:
            #当元素找不到的时候调用截图函数
            CapPic(self.driver)
            #元素找不到时在日志中记录信息
            logger.info(u'%s 页面中未找到 %s 元素' %(self,loc))

    def send_keys(self,loc,value):
        try:
            #获取元素的属性值，以便识别元素
            loc = getattr(self,"_%s" % loc)
            #查找元素并输入相关数据
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            # 当元素找不到的时候调用截图函数
            CapPic(self.driver)
            # 元素找不到时在日志中记录信息
            logger.info(u'%s 页面中未找到 %s 元素' % (self, loc))
    def click(self,loc):
        try:
            loc = getattr(self,"_%s" % loc)
            self.find_element(*loc).click
        except AttributeError:
            # 当元素找不到的时候调用截图函数
            CapPic(self.driver)
            # 元素找不到时在日志中记录信息
            logger.info(u'%s 页面中未找到 %s 元素' % (self, loc))
    # def moveto(self,loc):
    #     try:
    #         loc = getattr(self,"_%s" % loc)
    #         ActionChains(self.driver).move_to_element(*loc).perform()  # 对定位的元素执行悬停
    #
    #     except AttributeError:
    #         # 当元素找不到的时候调用截图函数
    #         CapPic(self.driver)
    #         # 元素找不到时在日志中记录信息
    #         logger.info(u'%s 页面中未找到 %s 元素' % (self, loc))
