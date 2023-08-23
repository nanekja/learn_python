
def filterEven(x):
    if x % 2 == 0:
        return False
    return True

def filterLower(x):
    if x == x.lower():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if (x>=90):
        return "A"
    elif (x>=65 and x <90):
        return "B"
    else:
        return "C"



    

def main():
    # Some sample sequences to operate on
    nums=(1,8,4,5,13,26,381,410,58,47)
    chars="abcDeFGHiJKlmnoP"
    grades=(81,89,94,78,61,66,99,74)

    # to filter and remove even numbers from the list
    odds = list(filter(filterEven, nums))
    print(odds)

    # to filter and remove all lower case letters
    upper = list(filter(filterLower, chars))
    print(upper)

    # map function is applied to a sequence
    squares = list(map(squareFunc, nums))
    print(squares)

    # sort and apply map to change numbers to grades
    grades=sorted(grades)
    letters=list(map(toGrade, grades))
    print(letters)



if __name__=="__main__":
    main()