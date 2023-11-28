#!/usr/bin/python3
for ascii_code in range(ord("a"), ord("z") +1):
    if ascii_code == ord("e") or ascii_code == ord("q"):
        continue
    print(chr(ascii_code), end="")
