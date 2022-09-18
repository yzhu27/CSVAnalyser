from tests import test_engine


if __name__ == '__main__':
    #TODO: Here to initial the with cli function (in utils), make user can modify the elements with cli
    test_engine.runs("ALL")
    exit(test_engine.fails)