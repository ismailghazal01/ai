import sys

if len(sys.argv) != 3:
    print("AssertionError")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        print("Sum:", a + b)
        print("Difference:", a - b)
        print("Product:", a * b)

        if b != 0:
            print("Quotient:", a / b)
            print("Remainder:", a % b)
        else:
            print("Quotient: ERROR")
            print("Remainder: ERROR")

    except:
        print("AssertionError")