import copy
import Cols
from Row import Row
# t is the parameter of 'fun'.

def csv(fname, fun, sep=','):
    src = open(fname)
    while True:
        s = src.readline()
        s = s[:-1]
        if s is None:
            return src.close()
        else:
            t = {}
            for s1 in s.split(sep):
                t[len(t)] = s1
            fun(t)
class Col:
    names = {}
    all = {}
    x = {}
    y = {}
    klass = {}
    names_index_mapping = {}
    def __init__(self,csv):
        self.names = csv.titles
        self.all = csv.cols
        index = 0
        for name in self.names:
            self.names_index_mapping[index] = name
            index = index+1
            if name in csv.cols_skip_index:
                continue
            elif name[len(name)-1]=='+':
                self.x[name] = csv.get_colum_by_index_with_skipped(name)
            elif name[len(name)-1]=='-':
                self.y[name] = csv.get_colum_by_index_with_skipped(name)
            else:
                self.klass[name] = csv.get_colum_by_index_with_skipped(name)


'''
class Data:
    def __init__(self, filename):
        csv = Csv()
        csv.read_csv(filename)
        self.cols = Cols(csv)
        self.rows = Row()

    # para1: x or y, # para2: mid or div
    def stats(self, places, para1, para2):
        col = self.cols

        if para1 == 'x':
            if para2 == 'mid':
                return 'x_mid'
            elif para2 == 'div':
                return 'x_div'
        elif para1 == 'y':
            if para2 == 'mid':
                return 'x_mid'
            elif para2 == 'div':
                return 'x_div'
'''



class Csv:
    cols = {}
    rows = {}
    cols_skip_index = set()
    row_skip_index = set()

    def __init__(self):
        cols = {}
        rows = {}
        row_skip_index = set()

    def read_csv(self, filename):
        file = open(filename)
        line = file.readline()
        line = line[:-1]
        self.titles = line.split(',')
        line = file.readline()
        # delete '\n'
        for string in self.titles:
            self.cols[string] = {}
        print(self.titles)
        cur_row = 0
        while line:
            line.strip()
            strs = line.split(',')
            index = 0
            self.rows[cur_row] = []
            for t in self.titles:
                if t[len(t) - 1] == ':':
                    self.cols_skip_index.add(t)
                    self.row_skip_index.add(index)
                    self.rows[cur_row].append(e)

                if t[0].isupper():
                    try:
                        e = strs[index]
                        num = float(e)
                        self.rows[cur_row].append(num)
                    except:
                        print("An parse exception with ", e)
                        num = e
                        self.rows[cur_row].append(num)
                        continue
                else:
                    self.rows[cur_row].append(e)
                index = index + 1
                self.cols[t][len(self.cols[t]) + 1] = num
            cur_row = cur_row + 1
            line = file.readline()

    def col_to_list(self, col_name):
        result = []
        for pair in self.cols[col_name]:
            result.append(self.cols[col_name][pair])
        return result

    def get_colum_by_index_with_skipped(self, col_name):
        if col_name in self.cols_skip_index:
            return None
        else:
            return self.col_to_list(col_name)

    def get_row_by_index_with_skipped(self, index):
        result = []
        for i in range(len(self.rows[index])):
            if i in self.row_skip_index:
                continue
            else:
                result.append(self.rows[index][i])
        return result


if __name__ == "__main__":
    csv = Csv()
    csv.read_csv(r"C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv")
    col = Col(csv)
    print(csv.titles)
    print('Elements in cols Clndrs: ', csv.cols['Clndrs'])  # select one col by col name(title)
    print(csv.cols['origin'][20])  # select specific element by col name and row number
    print(csv.cols['Hp:'])  # col name end with ':'--colon mark will have no element
    print(csv.col_to_list('Clndrs'))  # convert dicts K-V pair to list
    print('Elements in row 0: ', csv.rows[0])  # use row index to get certain row's elements
    print(csv.get_row_by_index_with_skipped(0))
    print(csv.get_colum_by_index_with_skipped('Clndrs'))

    print('Col names:', col.names)
    print('Col all', col.all)
    print('Col X:', col.x)
    print('Col Y', col.y)
    print('Col Klass', col.klass)
