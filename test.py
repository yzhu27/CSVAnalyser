import util_fun
from Num import Num
from Sym import Sym
from the import the



def test_the():
    util_fun.oo(the)
    assert True


def test_num():
    num = Num()
    for i in range(1, 101): num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    assert 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_sym():
    sym = Sym()
    for v in ["a", "a", "a", "a", "b", "b", "c"]: sym.add(v)
    mode = sym.mid()
    entropy = sym.div()
    entropy = (1000 * entropy) // 1/1000
    res={}
    res['mid'] = mode
    res['div'] = entropy
    util_fun.oo(res)
    assert mode == "a" and 1.37 <= entropy and entropy <=1.38

def test_bigNum():
    num = Num()
    the.nums = 32
    for i in range(1, 701): num.add(i)
    #util_fun.oo(num.nums())
    assert len(num._has) == 32

