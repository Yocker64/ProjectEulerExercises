try:
    #So this is actually a bad practice. You should only try the line of code where the problems can pop out
    x = int(input("what's x?"))
    print(f"x is {x}")
except ValueError:
    print("What you typed is not an integer")
