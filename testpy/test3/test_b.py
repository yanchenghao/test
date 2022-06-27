import pytest


@pytest.mark.run(order=2)
def test_bat(conf_fixture):
    print("sdsdfdsdfsdfsdfdfdfg")
    assert 1==2