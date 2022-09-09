#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    res = 0
    for i, item in enumerate(sys.argv[1:]):
        res += int(item)
    print(res)
