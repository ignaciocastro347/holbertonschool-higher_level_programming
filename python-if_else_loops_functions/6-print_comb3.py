#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{}{}".format(
            str(i) + str(j) if i < j else str(j) + str(i),
            "\n" if i == 8 and j == 9 else ", "),
            end="")
