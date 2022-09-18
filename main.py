from tests import test_engine


if __name__ == '__main__':
    test_engine.runs("ALL")
    exit(test_engine.fails)