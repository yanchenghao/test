import os
import random

import pytest
if __name__ == '__main__':
    # pytest.main(["./test2"])
    # a=random.randint(1,50)
    # pytest.main()
    # os.system(f"allure generate ./temp -o ./report --clean")
    pytest.main(['--clean-alluredir'])
    os.system(f"allure generate ./temp -o ./report --clean")