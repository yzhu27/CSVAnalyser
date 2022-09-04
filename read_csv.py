cols = {}

def readline(filename):
    file = open(filename)
    l = file.readline()
    titles = l.split(',')
    l = file.readline()
    for str in titles:
        cols[str] = {}
    while l:
        strs = l.split(',')
        x = 0
        for t in reversed(titles):
            if t[len(t) - 1] == ':':
                e = strs.pop()
                continue
            elif t[0].isupper():
                try:
                    e = strs.pop()
                    num = float(e)
                except:
                    print("An parse exception with ", e)
                    num = e
                    continue
            else:
                num = strs.pop()

            cols[t][len(cols[t]) + 1] = num
        l = file.readline()


if __name__ == "__main__":
    readline(r"C:\Users\Pinxiang Wang\Documents\PythonFileTransfer.csv")
    print(cols['Clndrs'])  # select one col by col name(title)
    print(cols['Volume'])
    print(cols['origin'][20])  # select specific element by col name and row number
    print(cols['Hp:'])  # col name end with ':'--colon mark will have no element
