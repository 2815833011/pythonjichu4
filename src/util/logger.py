from loguru import logger
import traceback
'''     日志类型
        +----------------------+------------------------+------------------------+
        | Level name           | Severity value         | Logger method          |
        +======================+========================+========================+
        | ``TRACE``            | 5                      | |logger.trace|         |
        +----------------------+------------------------+------------------------+
        | ``DEBUG``            | 10                     | |logger.debug|         |
        +----------------------+------------------------+------------------------+
        | ``INFO``             | 20                     | |logger.info|          |
        +----------------------+------------------------+------------------------+
        | ``SUCCESS``          | 25                     | |logger.success|       |
        +----------------------+------------------------+------------------------+
        | ``WARNING``          | 30                     | |logger.warning|       |
        +----------------------+------------------------+------------------------+
        | ``ERROR``            | 40                     | |logger.error|         |
        +----------------------+------------------------+------------------------+
        | ``CRITICAL``         | 50                     | |logger.critical|      |
        +----------------------+------------------------+------------------------+

'''
logger.add("log/debug.info") #添加保存日志文件路径
logger.info("输出信息")
logger.error("报错")
logger.warning("警告")
logger.success("成功")
logger.critical("严重报错")


'''

'''

#重写logger

class Loggers :
    __instance=None
    def __new__(cls):
          if not cls.__instance:
            cls.__instance= super().__new__(cls)
          return cls.__instance  

    def __init__(self,logfile="log/debug.info"):
            self.__log=logger
            self.__log.add(logfile)

    def info(self,msg):
          self.__log.info(msg)

    def error(self,msg):
          self.__log.error(msg)

    def warning(self,msg):
          self.__log.warning(msg)

    def success(self,msg):
          self.__log.success(msg)

    def critical(self,msg):
          self.__log.critical(msg)
        

#使用闭包函数封装log
dlog=Loggers()

def log(func):
      def log_action(*args,**kwargs):
            msg=f"执行函数:{func.__name__} 执行参数:"
            if args :
                  msg+=str(args[1::])
            if kwargs :
                  msg+=str(kwargs)

            dlog.info(msg)
            try:
                  retevl=func(*args,**kwargs)
            except:
                  dlog.error(f"执行失败{func.__name__}{traceback.format_exc()}")
            
            return retevl
      return log_action



if __name__=="__main__":
      # logger=Logger(function)
      pass