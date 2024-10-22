name = input("What's your name? ")

#with statement does open the file with the name you specify at the end of the line and whatever is indented below it
#knows the context that it is gonna open that file with that name, after that indentation it closes the file.
with open("texts/names.txt", "a") as file:
    file.write(f"{name}\n")