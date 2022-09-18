

from src.Cols import Cols, push
from src.Row import Row
from src.csv import csv
from src.Num import Num
from src.utils import rnd


class Data:
    def add(self,xs):
        if self.cols == None:
            value_list = list(xs.values())
            self.cols = Cols(value_list)
        else:
            row = Row(xs)
            row = push(self.rows,row)
            # need to be fixed
            for _, todo in enumerate([self.cols.x,self.cols.y]):
                #print(todo)
                for col in todo.values():
                    #print(type(col))
                    col.add(row.cells[col.at])

    #  not sure where to find the 'row' parameter.
    def __init__(self, src):
        self.cols = None
        self.rows = {}
        if type(src)==type('string'):
            csv(src,lambda row:self.add(row))
        else:
            for _,row in enumerate(src or {}):
                self.add(row)


    def stats(self,places,showCols, fun):
        showCols , fun = showCols or self.cols.y, fun or Num.mid()
        t = {};
        for col in showCols.values():
            v = fun(col)
            v = type(v) == type(0) and rnd(v,places) or v
            t[col.name] = v
        return t
