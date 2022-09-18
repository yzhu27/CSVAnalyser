from util_fun import o,oo
from Num import Num
from Sym import Sym
from the import the
from Data import Data
from Cols import Cols
from read_csv import csv
import random


fails=0

def runs(k):
    global eg
    if k not in eg.keys():
        return
    random.seed(the().config()["seed"])
    old=eg.copy()
    out = 3
    if the().config()["dump"]:
        out = eg[k]()
        status = True
    else: 
        try:
            out = eg[k]()
        except:
            status = False
        else:
            status = True
    eg=old.copy()
    if status:
        if out is True:
            msg = "PASS"
        else:
            msg = "FAIL"
    else:
        msg = "CRASH"
    print("!!!!!!!", msg, str(k), status)
    return out

def test_BAD():
    print(eg["none"])

def test_LIST():
    return sorted(eg.keys())

def test_LS():
    print("\nExamples lua csv -e ...")
    for k in test_LIST():
         print(str(k))
    return True

def test_ALL():
    global fails
    for k in test_LIST():
        if k != "ALL":
            print("\n-----------------------")
            if not runs(k):
                fails+=1
    return True
            
    


def test_the():
    oo(the().config())
    return True


def test_num():
    num = Num()
    for i in range(1, 101): num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

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
    return mode == "a" and 1.37 <= entropy and entropy <=1.38

def test_bignum():
    num = Num()
    num.the["nums"] = 32
    for i in range(1, 1000): num.add(i)
    oo(list(num.nums().values()))
    return len(num._has) == 32

row={}
n=0
def printer(row):
    global n
    if n <= 10:
        oo(list(row.values()))
        n+=1

def test_csv():
    csv(the().config()["file"], lambda row:printer(row))
    return True

def test_data():
    d = Data(the().config()["file"])
    for c in d.cols.y.values(): oo(c)
    return True

def test_stats():
    data = Data(the().config()["file"])
    print("xmid", o( data.stats(2, data.cols.x, lambda col:col.mid())))
    print("xdiv", o( data.stats(3, data.cols.x, lambda col:col.div())))
    print("ymid", o( data.stats(2, data.cols.y, lambda col:col.mid())))
    print("ydiv", o( data.stats(3, data.cols.y, lambda col:col.div())))
    return True

eg={"BAD": test_BAD,
    "LIST": test_LIST,
    "LS": test_LS,
    "ALL": test_ALL,
    "the": test_the,
    "num": test_num,
    "sym": test_sym,
    "bignum": test_bignum,
    "csv": test_csv,
    "data": test_data,
    "stats": test_stats}



if __name__ == '__main__':
    runs("ALL")
    exit(fails)