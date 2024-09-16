
from samplefile import add
from samplefile import multiply

def test_add():
    assert add(2,3) == 5
    assert add(-1, 1) == 0
    assert add(92,8) == 100

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(0,0) == 0
