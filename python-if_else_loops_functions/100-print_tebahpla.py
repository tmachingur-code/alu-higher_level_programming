#!/usr/bin/python3
for i in range(25, -1, -1):
    if (25 - i) % 2 == 0:
        print("{}".format(chr(97 + i)), end="")
    else:
        print("{}".format(chr(97 + i - 32)), end="")
