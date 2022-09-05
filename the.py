

import re


class the:
    def __init__(self) -> None:
        self.the = {}
        self.help = """CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:
        -e  --eg        start-up example                      = nothing
        -d  --dump      on test failure, exit with stack dump = false
        -f  --file      file with csv data                    = ../data/auto93.csv
        -h  --help      show help                             = false
        -n  --nums      number of nums to keep                = 512
        -s  --seed      random number seed                    = 10019
        -S  --seperator feild seperator                       = ,"""

    def coerce(self , s):
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

    def config(self):
        help = self.help
        res = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
        m = re.findall(res , help)
        for key , value in m:
            self.the[key] = self.coerce(value)
        

    def cli(self , t):
        for slot , v in t.items():
            v = str(v)

def main():
    The = the() 
    The.config()
    t = The.the
    print(t)
    

if __name__ == '__main__':
    main()


             