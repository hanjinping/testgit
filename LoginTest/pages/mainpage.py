import os.path
import time
from selenium.webdriver import ActionChains

from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from common.LogGen import LogGen
from selenium import webdriver
logger = LogGen(logger="MainPage").getlog()
# 定义主页面中所涉及到的元素，userID及退出按钮，通过xpath方式识别
class MainPage(BasePage):
    userid_loc = (By.XPATH,"/html/body/div[1]/section/header/div/div[2]/span/span")
    exit_btn_loc = (By.XPATH,"/html/body/div[1]/section/header/div/div[2]/div/div/div/ul/li[2]")
    #定义打开超链接方法，并将此操作写入日志
    def open(self,base_url):
        self._open(self.base_url,self.pagetitle)
        logger.info("打开链接：%s " % base_url)
    #定义显示userid信息，并将此操作写入日志
    def show_userid(self):
        userid = self.find_element(*self.userid_loc).text
        logger.info("当前用户ID是：%s" % userid)
        return userid
    #定义退出操作，点击退出按钮，并写入日志
    def exit_sys(self,driver):
        try:
            move = self.driver.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/span/i")  # 定位到要悬停的元素
            ActionChains(self.driver).move_to_element(move).perform()  # 对定位的元素执行悬停
            self.driver.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/div/div/div/ul/li[2]").click()
            time.sleep(5)
            link = self.driver.find_element_by_link_text("云效")
            if link:
                print("logout success!")
            else:
                print("logout fail!")
            time.sleep(5)
            self.driver.quit()
            logger.info("成功退出测试系统")
        except :
            logger.info("退出系统失败")

#
