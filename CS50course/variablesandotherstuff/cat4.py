def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("How many meows?"))
        if n > 0:
            return n

def meow(n):    
    for i in range(n):
        print("meow\n", end="")


main()