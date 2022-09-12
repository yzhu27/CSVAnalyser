

def o(d):
    return str(d).replace(":", "").replace(",", ":").replace("'", "")


def oo(d):
    print(o(d))
    pass


def csv_test(row):
    n=0
    if n>10:
        return True
    else:
        n+=1
        oo(row) 