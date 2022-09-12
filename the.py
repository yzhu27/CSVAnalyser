

import re



class the:
    def __init__(self) -> None:
        #Create a `the` variables
        self.the = {}
        #a header string showing help, from which I build the settings object
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
    
    # Handle Settings
    #Parse `the` config settings from `help`
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

    #build the settings object from help
    def config(self):
        help = self.help
        #match the contents like: '-e  --eg        start-up example                      = nothing'
        res = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
        m = re.findall(res , help)
        for key , value in m:
            self.the[key] = self.coerce(value)
        return self.the
        
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
                    t[slot] = self.coerce(v)
        #print 'help' after update
        if t['help']:
            print(self.help)
    
 
        

#main() function for unit test
def main():
    The = the()
    t = The.config()
    print(t)
    The.cli(t)
    print(t)
    

if __name__ == '__main__':
    main()


             