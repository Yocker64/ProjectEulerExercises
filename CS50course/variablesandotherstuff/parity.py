def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
# You can short this 4 lines of code the following way
# return True if n % 2 == 0 else False

# return n % 2 ==0

    if n % 2 == 0:
        return True
    else:
        return False

main()