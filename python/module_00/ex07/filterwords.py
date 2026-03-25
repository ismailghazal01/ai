import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
else:
    s = sys.argv[1]
    n = int(sys.argv[2])

    words = s.split()

    clean = []
    for w in words:
        w = w.strip(string.punctuation)
        if len(w) > n:
            clean.append(w)

    print(clean)