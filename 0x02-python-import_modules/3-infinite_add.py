#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    totl = 0
    for i in arguments:
        totl += int(i)
    print(totl)
