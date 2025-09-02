from functools import reduce


if __name__ == '__main__':
    print(reduce(lambda x, y : x * y, (x * x for x in range(1, 10) if x % 2 == 0)))