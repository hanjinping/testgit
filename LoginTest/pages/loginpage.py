from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from common.LogGen import LogGen
from common.GetUrl import GetUrl
logger = LogGen(logger='LoginPage').getlog()
#创建登录操作类，页面中的元素通过name,id,xpath方式识别
class LoginPage(BasePage):
    username = (By.ID,"username")
    password = (By.ID,"password")
    submit = (By.XPATH,"/html/body/div/div/div/div[1]/form/div[3]/div/div/span/button")
    #定义用户名元素识别及输入函数，并将此操作写入日志
    def input_username(self,username):
        self.find_element(*self.username).send_keys(username)
        logger.info("输入用户名：%s " % username)
    # 定义密码元素识别及输入函数，并将此操作写入日志
    def input_password(self,password):
        self.find_element(*self.password).send_keys(password)
        logger.info("输入用户名：%s " % password)
    # 定义提交按钮元素识别及输入函数，并将此操作写入日志
    def click_submit(self):
        self.find_element(*self.submit).click()
        logger.info("点击登录按钮")
