import logging

log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}

class Logger:
    def __init__(self,log_file,log_name,log_lever):
        self.log_file=log_file
        self.log_name=log_name
        self.log_lever=log_lever

        self.logger=logging.getLogger(log_name)#设置日志名称
        self.logger.setLevel(level=log_l[log_lever])#设置日志器的最低级别
        if not self.logger.handlers:#判断日志对象logger,是否创建了handers对象
            #创建handers生成文件和编码方式
            handle=logging.FileHandler(log_file,encoding='utf-8')
            #设置handers的日志最低级别
            handle.setLevel(log_l[log_lever])
            #设置日志信息格式化
            formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            #文件日志的编码方式
            handle.setFormatter(formatter)
            #创建handers输入到控制台
            console=logging.StreamHandler()
            # 设置控制台的日志最低级别
            console.setLevel(log_l[log_lever])
            #控制台的编码方式
            console.setFormatter(formatter)
            #将loggert添加handler
            self.logger.addHandler(handle)
            self.logger.addHandler(console)

            # self.logger.info("Start print logs")
            # self.logger.debug("Do something")
            # self.logger.warning("Something maybe fail.")
# a=Logger("test.log","test","info")
# a.logger.info("sdsdsd")
# a.logger.debug("sdsdsdsdsd")