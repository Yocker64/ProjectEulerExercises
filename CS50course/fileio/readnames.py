#Creates an empty array for storing the data
names = []

#Opens the file with the name "file"
with open("cs50course/fileio/texts/names.txt") as file:
#Appends every line stripping the last new line to the array of names
    for line in file:
        names.append(line.rstrip())
#Sorts the array names then it prints every line
for name in sorted(names):
    print(f"hello, {name}")