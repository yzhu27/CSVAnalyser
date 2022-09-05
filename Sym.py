import math

class Sym:
    def __init__(self,col,name):
        self.n = 0
        self.at = col
        self.name = name
        self.has = {} # Save values in a dictionary {value: number}

    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            if v in self.has:
                self.has[v] = self.has[v] + 1
            else:
                self.has[v] = 1

    def mid(self):
        most = -1
        for key in self.has:
            if self.has[key] > most:
                most = self.has[key]
                mode = key
        return mode

    def div(self):
        entropy = 0
        for key in self.has:
            if self.n != 0:
                p = self.has[key] / self.n
                entropy = entropy - p * math.log(p,2)
        return entropy
