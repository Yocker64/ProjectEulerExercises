from calculator import square

def main():
    test_square2()


def test_square2():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0




def test_square():
#This would be inefficient way to create unit tests but there's a better way using assert
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")

#Trying to see wether the assertion that square of 2 is 4 holds, if not print the error message in order
#tell the user what went wrong
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")


if __name__ == "__main__":
    main()