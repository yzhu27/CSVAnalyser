import math

def o(d):
    return str(d).replace("[","{").replace("]","}").replace("'", "")


def oo(d):
    print(o(d))
    pass

    

# Handle Settings
#Parse `the` config settings from `help`
def coerce(s):
    def fun(s1):
        if s1 == 'true':
            return True
        if s1 == 'false':
            return False 
        return s1.strip()
    if s.isdigit():
        return int(s)
    try:
        tmp = float(s)
        return tmp
    except ValueError:
        return fun(s)

def copydic(t):
    """
    For dictionary t, return the deep copy of t; otherwise return t.
    """

    if ~isinstance(t,dict):
        return t
    u = {}
    for k in t:
        u[k] = copydic(t[k])
    return u


# line 62
# add x to t, return x
def push(t, x):
    t[len(t)] = x
    return x

def rnd(x,places):
    mult = pow(10,(places or 2))
    return math.floor(x * mult +0.5)/mult



n=0
def print_counter(row):
    global n
    if n <= 10:
        oo(list(row.values()))
        n+=1
