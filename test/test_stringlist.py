import pytest

@pytest.fixture
def stringlist():
    return ["a","b","c"]


def test_length(stringlist):
    assert(len(stringlist)==3)

def test_first(stringlist):
    assert('a' == stringlist[0])

def test_second_f(stringlist):
    assert('b' == stringlist[1])    

@pytest.mark.parametrize("slist", [(["a","b","c","d"]),(["b","b","d","d"]),(["a","b","c","d"])])
def test_eval(slist):
    assert( len(slist)==4)