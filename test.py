import pytest
from main import sum2

@pytest.mark.parametrize('a,b,result',
                         [
                             (3, 3, 9),
                             (4, 3, 13),
                             (5, 3, 15)
                         ])
def test_sum2(a, b, result):
    assert sum2(a, b) == result
