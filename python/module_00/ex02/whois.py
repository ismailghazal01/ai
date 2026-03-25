import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
else:
    try:
        n = int(sys.argv[1])

        if n == 0:
            print("I'm Zero.")
        elif n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except:
        print("AssertionError: argument is not an integer")