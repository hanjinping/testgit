import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Login():
    def brower_start(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

    def login(self,uname, pwd):
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div[3]/div/div/span/button")
        username.send_keys(uname)
        password.send_keys(pwd)
        submit.click()
        time.sleep(5)
        userid = self.driver.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/span/span")
        if userid.text == "hanjinping":
            print("login success!")
        else:
            print("login fail!")
            self.driver.quit()

    def logout(self):
        move = self.driver.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/span/i")  #定位到要悬停的元素
        ActionChains(self.driver).move_to_element(move).perform() #对定位的元素执行悬停
        self.driver.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/div/div/div/ul/li[2]").click()
        time.sleep(5)
        link = self.driver.find_element_by_link_text("云效")
        if link:
            print("logout success!")
        else:
            print("logout fail!")

        time.sleep(5)
        self.driver.quit()

# test = Login()
# test.brower_start("http://mqc.test.haigeek.com/login")
# test.login("hanjinping", "hjp123456H.")
# test.logout()