# class Num
# return kept numbers, sorted

from operator import truediv
#import math for using min() and max(), etc
import math
# import random for randomly delete an element once the room is full
import random

from src.the import the


# line 59 function per(t, p)
# this function returns the pth element of the sorted list t
def per(t, p):
    if(p>0 and p<1):
        p = math.floor(len(t)*p)
    return t[p]
    
class Num:
    
    ## line 124 function Num:new(c,s)
    def __init__(self, c=0, s=""):
        self.n = 0 # items seen
        self.at = c # column position
        self.name = s # column name        
        self._has = {} # dict for keeping data
        
        self.lo = math.inf # lowest seen
        self.hi = -math.inf # highest seen
        self.isSorted = True # no updates since last sort of data
        self.w = 1 # not yet
        
        THE = the()     
        self.the = THE.config() 
    
    # line 178 function Num:add(v,    pos)
    def nums(self):
        if self.isSorted == False:
            sorted(self._has.items(), key = lambda dc:(dc[1], dc[0]))
            self.isSorted == True
        return self._has
    
    # line 182 function Num:add(v,    pos)
    # accoding to the rotation at line 17, pos should be a local?
    # but here treats it as a normal variable
    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            self.lo = min(float(v), self.lo)
            self.hi = max(float(v), self.hi)
            pos = -1
            
            # line 189: have no idea about what the.nums is, it should be an integer
            if len(self._has) < self.the['nums']:
                pos = len(self._has)
            elif random.random() < self.the['nums']/self.n:
                pos = random.randint(0, len(self._has)-1)
            
            if pos > -1:
                self.isSorted = False
                self._has[pos] = int(float(v))
    
    
    
    # line 194 function Num:div(    a)
    # this function returns the Standard Deviation for Nums, or entropy for Syms
    # here should be SD of a
    def div(self):
        a = self.nums()
        return (per(a,0.9) - per(a,0.1)) / 2.58
    
    # line 197 Num:mid()
    # this function returns the median for Nums, or mode for Syms
    def mid(self):
        return per(self.nums(), 0.5)

    def __str__(self):
        D={}
        D["at"]=self.at
        D["hi"]=self.hi
        D["isSorted"]=self.isSorted
        D["lo"]=self.lo
        D["n"]=self.n
        D["name"]=self.name
        D["w"]=self.w
        return str(D)

