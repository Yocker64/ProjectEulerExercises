def main():
    hello("world")
    goodbye("world")
#Something interesting is happening here
#When you run a file from the command line and you are running the function is defined in the file the name of the 
#variable  __name__ will be  __name__ in other case you are gonna have the name of the varialbe equal to the 
#the name of the class in this case it the variable will be sayings if you run the file say1.py
def hello(name):
    print(f"hello, {name}")
    print(__name__)

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    print(__name__)
    main()
