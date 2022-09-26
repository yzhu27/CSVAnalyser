import math


class Sym:
    
    def __init__(self,col=0,name=""):
        self.n = 0
        self.at = col
        self.name = name
        self.has = {} # Save values in a dictionary {value: number}
        
        

    def add(self, v):
        
        """
        Add symbolic value v to given column. If dictionary has contains key v, add 1 to its value; otherwise add key v to has with value 1.
        """
        
        if v != "?":
            self.n = self.n + 1
            if v in self.has:
                self.has[v] = self.has[v] + 1
            else:
                self.has[v] = 1

                
                
    def mid(self):
        
        """
        Return the most common value in this symbolic column.
        """
        
        most = -1
        for key in self.has:
            if self.has[key] > most:
                most = self.has[key]
                mode = key
        return mode
    
    

    def div(self):
        
        """
        Calculate entropy of the symbolic column.
        """
        
        #edited by Lognam, but still cannot get the correct result at the present
        entropy = 0
        for key in self.has:
            if key > 0:
                p = key / self.n
                funP = p * math.log(p,2)
                entropy = entropy - funP
        return entropy

