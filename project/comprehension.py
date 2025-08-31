from functools import reduce

print(reduce(lambda x, y : x * y ,list(x for x in range(1, 12) if x % 2 != 0)))

print(reduce(lambda x, y : x * y, (x for x in range(1, 11) if x %2 == 0)))