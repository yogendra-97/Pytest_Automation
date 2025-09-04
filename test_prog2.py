import pytest


@pytest.mark.test

def test_firstProgram():
    msg = "Hello"
    assert "He" in msg, "Test failed because strings do not match"

def test_SecondProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
    
def test_dfef():
    assert 2==2

