#Import the csv library that helps me to handle csv files, this is a library from python itself
import csv
#We are gonna use dictionaries instead of lists because using dictionaries is better for handling data
#in cases like we want to change the distribution of the csv file we can do it more easily because
#we just arrange the data taking into consideration the headers and we don't have to worry about the code, the code will still work regardless of the passage of times
#Creates an empty dictionary, not a list
students = []
#Opens the file
with open("texts/students2.csv") as file:
#Reads the file as a dictionary that is why on the csv file the header has the name of the data stored in the colums
    reader = csv.DictReader(file)
#Now that we have the dictionary we can scroll through the rows (the keys and values) to print the info we want
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
#Creates a lambda funciont that sorts the dictionary in alphabetic order taking as the input the name of the student
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} if from {student['home']}")