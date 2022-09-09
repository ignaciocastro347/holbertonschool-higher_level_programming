#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    print("{} argument{}".format(
        len(argv) - 1,
        "s" if len(argv) - 1 != 1 else "",
        ":" if len(argv) - 1 != 0 else "."))
    for i, item in enumerate(argv):
        if i != 0:
            print("{}: {}".format(i, item))
