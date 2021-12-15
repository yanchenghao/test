# import logging
# import os
# import pytest
#
# from common import yaml_conf
#
# log_l={
#     "info":logging.INFO,
#     "debug":logging.DEBUG,
#     "warning":logging.WARNING,
#     "error":logging.ERROR
# }
#
# class Logger:
#     def __init__(self,log_file,log_name,log_lever):
#         self.log_file=log_file
#         self.log_name=log_name
#         self.log_lever=log_lever
#
#         self.logger=logging.getLogger(log_name)
#         self.logger.setLevel(level=logging.INFO)
#         if not self.logger.handlers:#判断日志对象logger,是否创建了handers对象
#             handle=logging.FileHandler(log_file)
#             handle.setLevel(log_l[log_lever])
#             formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#             handle.setFormatter(formatter)
#             console=logging.StreamHandler()
#             console.setLevel(log_l[log_lever])
#             console.setFormatter(formatter)
#             self.logger.addHandler(handle)
#             self.logger.addHandler(console)
#
#             # self.logger.info("Start print logs")
#             # self.logger.debug("Do something")
#             # self.logger.warning("Something maybe fail.")
# a=Logger("test.log","test","info")
# a.logger.info("sdsdsd")
# a.logger.debug("sdsdsdsdsd")
# print(os.path.dirname(__file__))
# print(__file__)
# print(os.path.split(__file__)[-1])
# print(os.path.split(__file__)[-1].split(".")[0])
# print(os.path.dirname(__file__))
# # sd=[1,2,3]
# # @pytest.mark.parametrize("sss", sd)
# # def test_dfdf(sss):
# #     print(sss)
# # test_dfdf
