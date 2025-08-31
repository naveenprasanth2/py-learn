from functools import reduce

print(reduce(lambda x, y : x * y, (x for x in range(1, 11) if x %2 == 0)))