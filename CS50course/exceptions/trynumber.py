try:
    x = int(input("what's x?"))
    print(f"x is {x}")
except ValueError:
    print("What you typed is not an integer")
    