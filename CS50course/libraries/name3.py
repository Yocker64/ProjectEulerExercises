import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#We are taking a slice of the array starting from the index 1 to the final, you don't have to write a second number in the brackets
#If we happen to write sys.argv[1:-1]:, the program will print from index 1 of the array to the value previous to the final 
for arg in sys.argv[1:]:
    print("Hello, my name is",arg)

