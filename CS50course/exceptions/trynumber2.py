def main():
    message = get_int()
    print(f"x is {message}")

#We are gonna create a function that gets integers
def get_int():
    # We don't necessarily have to exit the input face just trying once
    while True:
        #We are gonna try to get an input from the user
        try:
            #You could use "return int(""What's x?)" to make the code even more compact and save the final 2 lines of code of the function
            x = int(input("What's x?"))
        #We are gonna handle the type of Exception ValueError which happens when you don't get type of input a function was expecting
        except ValueError:
            #You can use the word "pass" in order to just dont print no error message and try again the input
            print("x is not an integer")
        #If nothing goes wrong then do the following (in this case, going outside of the loop)
        else:
            return x
    

main() 