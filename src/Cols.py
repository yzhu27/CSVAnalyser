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

    # following constructor is written by WPX, commented by HJY
    def initTest(self, csv):
        self.names = csv.titles # all column names        
        self.all = csv.cols #all the columns, including the skipped ones
        # notice that the input is no longer names, but a csv file readed in data
        
        
        self.klass = {}
        # the single dependent klass column, if it exists
        # notice that it is "nil" in lua, here it is a dict
        
        self.x = {} # independent columns, which are not skipped
        self.y = {} # dependent columns, which are not skipped
        
                
        for name in self.names:
            lenOfNames = len(name)
            if name in csv.cols_skip_index:
                continue 
                # whether the col should be skipped is determined by checking a list in csv
            elif name[lenOfNames-1] == '+':
                self.x[name] = csv.get_colum_by_index_with_skipped(name)
                # '+' if the dependent needs to be maximized
                # whether this should be involved into x is not sure
            elif name[lenOfNames-1] == '-':
                self.y[name] = csv.get_colum_by_index_with_skipped(name)
                # '-' if the dependent needs to be minimized
                # whether this should be involved into y is not sure
            else:
                self.klass[name] = csv.get_colum_by_index_with_skipped(name)
                # according to the lua code, klass should relate to cols whose last character is '!
                # however, there are not such a kind of column in the csv file
                # whether this should be involved into klass is not sure
