students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Rusell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
students[3]["patronus"]= "hola"

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")