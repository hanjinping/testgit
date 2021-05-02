import time
import os
def CapPic(driver):
    pt=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
    #  print(pt)
    picname=os.path.dirname(os.path.abspath('.'))+'\\picture\\'+pt+'.png'
    #  print(picname)
    driver.get_screenshot_as_file(picname)