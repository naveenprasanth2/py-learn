from functools import reduce

def test(*args):
    return reduce(lambda x, y : x * y, [x ** x for x in args])

print(test(1,2,3,11))