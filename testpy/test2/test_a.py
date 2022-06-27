import pytest


# pytest.skip("跳过整个模块", allow_module_level=True)
# @pytest.mark.run(order=1)
class Testhello():
    @pytest.mark.run(order=4)
    def test_cat(self):
       # if 1<2:
       #     pytest.skip("1<2")
       print("11111")

    a = 2
    @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="还没有完成用例")
    @pytest.mark.skipif(a==2,reason="触发了条件就可以跳过")
    def test_dog(self):
        print("222222")

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_pig(self):
       print("333333")

    @pytest.mark.run(order=2)
    def test_chicken(self):
       print("4444444444")
