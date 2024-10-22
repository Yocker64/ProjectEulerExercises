with  open("texts/students.csv") as file:
    for line in file:
#Getting the row and then splitting it when it encounters a "," then putting those values in a list
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")