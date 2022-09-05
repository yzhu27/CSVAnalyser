import copy

cols = {}
rows = {}
row_skip_index = set()

def read_csv(filename):
    file = open(filename)
    line = file.readline()
    titles = line.split(',')
    line = file.readline()
    for string in titles:
        cols[string] = {}
    cur_row = 0
    while line:
        strs = line.split(',')
        index = 0
        rows[cur_row] = []
        for t in titles:
            if t[len(t) - 1] == ':':
                e = strs[index]
                row_skip_index.add(index)
                rows[cur_row].append(e)
                continue
            elif t[0].isupper():
                try:
                    e = strs[index]
                    num = float(e)
                    rows[cur_row].append(num)
                except:
                    print("An parse exception with ", e)
                    num = e
                    rows[cur_row].append(num)
                    continue
            else:
                num = strs.pop()
                rows[cur_row].append(e)
            index = index + 1
            cols[t][len(cols[t]) + 1] = num
        cur_row = cur_row + 1
        line = file.readline()


def col_to_list(col_name):
    result = []
    for pair in cols[col_name]:
        result.append(cols[col_name][pair])
    return result


if __name__ == "__main__":
    read_csv(r"C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv")
    print('Elements in cols Clndrs: ',cols['Clndrs'])  # select one col by col name(title)
    print(cols['origin'][20])  # select specific element by col name and row number
    print(cols['Hp:'])  # col name end with ':'--colon mark will have no element
    print(col_to_list('Clndrs')) # convert dicts K-V pair to list
    print('Elements in row 0: ',rows[0]) # use row index to get certain row's elements


