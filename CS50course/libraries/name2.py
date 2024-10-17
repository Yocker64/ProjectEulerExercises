import sys
if len(sys.argv) < 2:
    #One can use sys.exit("bluh bluh bluh") in order to finish the execution of the program prematurely
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello my name is", sys.argv[1])