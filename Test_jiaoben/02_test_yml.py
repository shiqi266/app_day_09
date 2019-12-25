import pytest
import os,sys
sys.path.append(os.getcwd())

from Base.getData import Gget


def get_sum_data():
    sum_list = []
    data =Gget().a_get("sum.yml")
    for i in data.values():
        sum_list.append(tuple(i.values()))
        print(sum_list)
    return sum_list


# get_sum_data()

# [({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 3, 'c': 4}, {'a': 5, 'b': 2, 'c': 7})]

class Test_add():
    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_addf(self,a,b,c):
        assert a+b == c


if __name__ == '__main__':
    pytest.main(['02_test_yml.py'])