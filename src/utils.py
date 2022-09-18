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

#Update settings from values on command-line flags. Booleans need no values
def cli(self , t):
    tmp = input()
    #store the input command
    slots = list(tmp.split())
    #search the key and value we want to update
    for slot , v in t.items():            
        #give each imput slot an index(begin from 0)
        for n , x in enumerate(slots):
            # match imput slot with the.keys: x == '-e' or '--eg'
            if x == ('-'+slot[0]) or x == ('--'+slot):
                v = str(v)
                #we just flip the defeaults
                if v == 'True':
                    v = 'false'
                elif v == 'False':
                    v = 'true'
                else:
                    v = slots[n+1]
                t[slot] = coerce(v)
    #print 'help' after update
    if t['help']:
        print(self.help)

n=0
def print_counter(row):
    global n
    if n <= 10:
        oo(list(row.values()))
        n+=1
