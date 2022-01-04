# def setup_module():
#     print("==>setup_module")
# 模块级别 --对这个文件起作用，所有测试类之后执行
def setup_module():
    print("==>teardown_module")
def teardown_module():
    print("==>teardown_module")
def setup_class(self):
        print("==>setup_class1")
    #类级别结束--类里面所有方法之后执行
def teardown_class(self):
        print("==>teardown_class1")
    #方法级开始--类里每个测试方法执行前执行
def setup(self):
        print("-->setup_method1")
    #方法级结束--类里每个测试方法执行后执行
def teardown(self):
        print("-->teardown_method1")

def setup_method(self):
    print("-->setup_method1")
# 方法级结束--类里每个测试方法执行后执行
def setup_method(self):
    print("-->teardown_method1")
def setup_function(self):
    print("-->setup_method1")
# 方法级结束--类里每个测试方法执行后执行
def setup_function(self):
    print("-->teardown_method1")