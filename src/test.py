from util_fun import o,oo
from Num import Num
from Sym import Sym
from the import the
from Data import Data
from Cols import Cols
from read_csv import csv


def test_the():
    oo(the)
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
    oo(res)
    assert mode == "a" and 1.37 <= entropy and entropy <=1.38

def test_bigNum():
    num = Num()
    num.the["nums"] = 32
    for i in range(1, 700): num.add(i)
    oo(num.nums())
    assert len(num._has) == 32

row={}

def test_csv():
    t=the().config()
    csv(t["file"], lambda row:oo(row))
    assert True

def test_data():
    d = Data(the().config()["file"])
    for c in d.cols.y.values(): oo(c)
    assert True

def test_stats():
    data = Data(the().config()["file"])
    print("xmid", o( data.stats(2, data.cols.x, lambda col:col.mid())))
    print("xdiv", o( data.stats(3, data.cols.x, lambda col:col.div())))
    print("ymid", o( data.stats(2, data.cols.y, lambda col:col.mid())))
    print("ydiv", o( data.stats(3, data.cols.y, lambda col:col.div())))
    assert True
