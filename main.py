import sys
from tests import test_engine
from src.the import the 
from src.the import cli





if __name__ == '__main__':
    #TODO: Here to initial the with cli function (in utils), make user can modify the elements with cli
    list_of_argument = sys.argv
    the = cli(the , list_of_argument)
    test_engine.runs(the["eg"])
    exit(test_engine.fails)