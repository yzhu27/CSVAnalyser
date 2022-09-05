import util_fun
import Num
import Sym

def the():
    util_fun.oo(the)
    assert True


def num(num, mid, div):
    num = Num()
    for i in range(1, 101): num.add(i)
    mid = num.mid()
    div = num.div()
    #print(mid, div)
    assert 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def sym(sym, entropy, mode):
    sym = Sym()
    for v in ["a", "a", "a", "a", "b", "b", "c"]: sym.add(v)
    mode = sym.mid()
    entropy = sym.div()
    entropy = (1000 * entropy) // 1/1000
    #util_fun.oo(mid = mode, div = entropy)
    assert mode == "a" and 1.37 <= entropy and entropy <=1.38

def bigNum(num):
    num = Num()
    the.num = 32
    for i in range(1, 101): num.add(i)
    #util_fun.oo(num.nums())
    assert len(num._has) == 32


