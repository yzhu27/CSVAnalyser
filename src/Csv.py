from src.the import the
import csv
from src.utils import coerce
# t is the parameter of 'fun'.

def csv(fname, fun):
    sep = the["seperator"]
    
    #src = open(fname)
    with open(fname,'r') as src:
        rdr = csv.reader(src, delimiter=sep)
        for l in rdr:
            d={}
            for v in l:
                d[len(d)]=coerce(v)
            #print(d)
            fun(d)

