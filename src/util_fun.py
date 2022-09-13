

def o(d):
    return str(d).replace(":", "").replace(",", ":").replace("'", "")


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