import math

from Cols import Cols, push
from Row import Row
from read_csv import Csv, csv

def rnd(x,places):
    mult = pow(10,(places or 2))
    return math.floor(x * mult +0.5)/mult

class Data:
    def add(self,xs,row):
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or Row(xs))
            for _,todo in enumerate(self.cols.x,self.cols.y):
                for _,col in enumerate(todo):
                    col.add(row.cells[col.at])

    # 't' is not in the lua code, but not sure where to find the 'row' parameter.
    def __init__(self, src,t):
        self.cols = None
        self.rows = {}
        if type(src)==type('string'):
            csv(fname=src,fun=self.add(),t=t.row)
        else:
            for _,row in enumerate(src or {}):
                self.add(row)


    def stats(self,places,showCols, fun, t,v):
        showCols , fun = showCols or self.cols.y, fun or "mid"
        t = {};
        for _, col in enumerate(showCols):
            v = fun(col)
            v = type(v) == type(0) and rnd(v,places) or v
            t[col.name] = v
        return  t

if __name__ == '__main__':
    data = Data("C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv",)