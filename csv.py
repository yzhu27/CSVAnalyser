import copy


# ‘Row‘ holds one record
class Row:
    def __init__(self, t):
        self.cell = t,  # one record
        self.cooked = copy.deepcopy(t)  # used if we discretize data
        self.isEvaled = False  # true if y−values evaluated


# ‘Columns‘ Holds of summaries of columns.
# Columns are created once, then may appear in multiple slots.
class Cols:
    names = []  # all column names
    all = []  # all the columns (including the skipped ones)
    klass = None  # the single dependent klass column (if it exists
    x = []  # independent columns (that are not skipped)
    y = []  # dependent columns (that are not skipped)

    def __init__(self, names):
        self.names = names
        # -------unfinished


# ‘Num‘ summarizes a stream of numbers
class Num:  # c--col, s--symbol
    def __init__(self, c, s):
        self.n = 0
        self.at = c or 0
        name = s or " "
        _has = []  # as per Symbol
        low = min()  # lowest seen
        high = max()  # highest seen
        isSorted = True  # no updates since last sort of data
        w = ((s or "").find("-$" and -1 or 1))  # <---------- Unknown Parameter ????


# ‘Data‘ is a holder of ‘rows‘ and their summaries (in ‘cols‘).
class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if type(src) == str:
            csv(src, Row())


# ‘Sym‘s summarize a stream of symbols.
class Sym:
    def __init__(self, c, s):
        self.n = 0  # items seen
        self.at = c or 0  # column position
        self.name = s or "",  # column name
        _has = {}  # kept data


# Call ‘fun‘ on each row. Row cells are divided in ‘the.seperator‘.
def csv(filename, fun):
    sep = ','
    src = open(filename)
    while True:
        s = src.readline()
        if s is None:
            return src.close()
        else:
            t = []
            for s1 in s.split(sep):
                t.append(coerce(s1))
            fun(t)


# to parse data
def coerce(s, fun):
    def fun(s1):  # parse boolean
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1

    return float(s)  # -----------unfinished. csv.lua line 26


def readline(filename):
    file = open(filename)
    l = file.readline()
    while l:
        strs = l.split(',')
        x = 0
        for num in strs:
            print(num + ',')
        print('\n')
        l = file.readline()


if __name__ == "__main__":
    readline(r"C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv")
