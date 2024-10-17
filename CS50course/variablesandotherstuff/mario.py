def main():
    print_column(3)
    print_row(5)
    print_rectangle(5,4)

#Prints a column of # of height "height"
def print_column(height):
    print("#\n" * height, end="")

#Prints a row of ? of lenght "length"
def print_row(width):
    print("#" * width)


def print_rectangle(height, width):
    for rows in range(height):
        print_row(width)


main()