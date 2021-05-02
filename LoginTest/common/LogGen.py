import logging
import os
import time
class LogGen(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        # log常用四个级别优先级从高到低依次是ERROR、WARN、INFO、DEBUG
        # 创建Handler写到文件中
        lt = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        #  logname = os.path.dirname(os.path.abspath('.'))+'\\logs\\' + lt + '.log'
        logname = os.path.abspath('.') + '\\logs\\' + lt + '.log'
        fileh = logging.FileHandler(logname)
        fileh.setLevel(logging.INFO)
        # # 创建Handler写到控制台
        consoleh = logging.StreamHandler()
        consoleh.setLevel(logging.INFO)

        # 日志内容格式化
        formattest = logging.Formatter('%(asctime)s %(name)s[line:%(lineno)d] %(levelname)s %(message)s')
        fileh.setFormatter(formattest)
        consoleh.setFormatter(formattest)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)
        #  logger.info('hello,first test')

    def getlog(self):
        return self.logger
