def copy(t):
    """
    For dictionary t, return the deep copy of t; otherwise return t.
    """

    if !isinstance(t,dict):
        return t
    u = {}
    for k in t:
        u[k] = copy(t[k])
    return u

    
    
class Row:
    def __init__(self,t={}):
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False
