import re
from src.utils import coerce


#build the settings object from help
def config(the):
    #match the contents like: '-e  --eg        start-up example                      = nothing'
    res = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    m = re.findall(res , help)
    for key , value in m:
        the[key] = coerce(value)
    return the

#Update settings from values on command-line flags. Booleans need no values
def cli(t):
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
        print(help)
    return t

help = """CSV : summarized csv file
    (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
    USAGE: lua seen.lua [OPTIONS]
    OPTIONS:
    -e  --eg        start-up example                      = nothing
    -d  --dump      on test failure, exit with stack dump = false
    -f  --file      file with csv data                    = ./data/auto93.csv
    -h  --help      show help                             = false
    -n  --nums      number of nums to keep                = 512
    -s  --seed      random number seed                    = 10019
    -S  --seperator feild seperator                       = ,"""
        
the = {}
the = config(the)



    
 
        

# #main() function for unit test
# def main():
#     The = the()
#     t = The.config()
#     print(t)
#     The.cli(t)
#     print(t)
    

# if __name__ == '__main__':
#     main()


             