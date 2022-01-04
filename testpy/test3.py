
def runmore(function):
    def get_run_andmore(*args,**kwargs):
        print("开始跑步")
        function(*args,**kwargs)
    return get_run_andmore#不加括号
@runmore
def run(a):
    print(a)

run(a="sdsd2222")