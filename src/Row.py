from src.utils import  copydic
    
    
class Row:
    def __init__(self,t={}):
        self.cells = t
        self.cooked = copydic(t)
        self.isEvaled = False