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

        self.logger=logging.getLogger(log_name)
        self.logger.setLevel(level=logging.INFO)
        if not self.logger.handlers:#判断日志对象logger,是否创建了handers对象
            handle=logging.FileHandler(log_file)
            handle.setLevel(log_l[log_lever])
            formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handle.setFormatter(formatter)
            console=logging.StreamHandler()
            console.setLevel(log_l[log_lever])
            console.setFormatter(formatter)
            self.logger.addHandler(handle)
            self.logger.addHandler(console)

            # self.logger.info("Start print logs")
            # self.logger.debug("Do something")
            # self.logger.warning("Something maybe fail.")
# a=Logger("test.log","test","info")
# a.logger.info("sdsdsd")
# a.logger.debug("sdsdsdsdsd")