import sys

try:
    print("Hello, my name is ", sys.argv[1])
    #If you did not specify the index one before running the code there a IndexError is gonna pop out
except IndexError:
    print("Too few arguments")
    #You could use if to handle the issue and see if the array has enough index
    #You don't have to use the exception handle, you can take a smarter approach using if