import pytest

data = [("username1", "password1"), ("username2", "password2")]
@pytest.fixture(scope="function",params=data)
def my_fixture(request):
    return request.param

@pytest.fixture(scope="function")
def you_fixture():
    print("这个是前置的方法")
    yield
    print("这个是后置的方法")
    #
class TestMashang:
     def test_01_baili(self,my_fixture,you_fixture):
          print(f"{my_fixture[0]}的密码是{my_fixture[1]}")

     # def test_01_yao(self, my_fixture):
     #     print("\n测试瑶")
