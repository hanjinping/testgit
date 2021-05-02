from common.ReadConfig import GetBrowserInfo
from common.CapPic import CapPic
from common.LogGen import LogGen
from selenium import webdriver
import os
logger = LogGen(logger='浏览器启动加载').getlog()
def BrowserStart():
    browsername = GetBrowserInfo("BrowserName")
    url = GetBrowserInfo('Url')
    if browsername == 'Chrome':
        logger.info('启动Chrome浏览器')
        driver = webdriver.Chrome()
    if browsername == 'Firefox':
        logger.info('启动Firefox浏览器')
        driver = webdriver.firefox()
    if browsername == 'IE':
        ogger.info('启动IE浏览器')
        driver = webdriver.ie()
    logger.info('打开测试网页')
    driver.get(url)
    CapPic(driver)
BrowserStart()
