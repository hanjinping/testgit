import configparser #python自带的配置文件处理函数
import os  #读取当前配置文件所在路径
def GetBrowserInfo(info):
    cf=configparser.ConfigParser()
    cfpath=os.path.dirname(os.path.abspath('.'))+"\\config\\config.ini"
    #os.path.abspath('.')获得当前文件的目录路径
    #os.path.dirname(）获得当前目录的上级目录
    cf.read(cfpath)
    browserinfo = cf.get('browser',info)
    return browserinfo

# print(GetBrowserName("BrowserName"))
