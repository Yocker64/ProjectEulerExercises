name = input("What's your name?")

#The line below opens the file called names.txt and opens it in a way that allows me to "w"rite in the file
file = open("texts/names.txt", "w")
#Writes the name in the file
file.write(name)
#Closes the file
file.close()