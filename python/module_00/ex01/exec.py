import sys

if len(sys.argv) <= 1:
    pass
else:
    s = ""
    for i in range(1, len(sys.argv)):
        if i > 1:
            s += " "
        s += sys.argv[i]

    res = ""
    for c in s:
        if c.islower():
            res += c.upper()
        else:
            res += c.lower()

    print(res[::-1])