from logging import NullHandler
import copy

from Sym import Sym
from Num import Num

# line 62
# add x to t, return x
def push(t, x):
    t[len(t)] = x
    return x
class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = {}
        self.x = {}
        self.y = {}
        
        for index, name in enumerate(names):
            # all columns should be recorded in self.all, including those skipped columns
            # if the column starts with a capital character, it is Num
            # otherwise, it is Sym
            if name.istitle():
                curCol = push(self.all, Num(index, name))
            else:
                curCol = push(self.all, Sym(index, name))    
            
            # lenOfName = len(name)
            
            # if a column ends with a ':', the column should be skipped and recorded nowhere except self.all
            
            # if there is any '+' or '-', the column should be regarded as a dependent variable
            # all dependent variables should be recoreded in self.y
            # on the contrary, those independent variables should be recorded in self.x
            if name[-1] != ":":
                if "+" in name or "-" in name:
                    push(self.y, curCol)
                else:
                    push(self.x, curCol)
                
                # if a column name ends with a '!', this column should be recorded AS self.klass
                # NOTICE THAT IT IS "AS", NOT "INCLUDED IN"
                if name[-1] == "!":
                    self.klass = name