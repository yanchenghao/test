import pytest
a=[1,2]
b=[3,4]
@pytest.mark.parametrize("a",a)
@pytest.mark.parametrize("b",b)
def test_islen1(a,b):
  print(a)
  print(b)