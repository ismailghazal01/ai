import random

num = random.randint(1, 99)

while True:
    guess = input(">> ")

    if guess == "exit":
        break

    try:
        g = int(guess)
        if g < num:
            print("Too low")
        elif g > num:
            print("Too high")
        else:
            print("Correct")
            break
    except:
        print("Not a number")