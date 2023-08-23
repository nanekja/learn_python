# use lambdas as in-place functions

def Celsius2Fahrenheit(temp):
    return (temp*9/5) + 32

def Fahrenheit2Celsius(temp):
    return (temp-32)*5/9


def main():
    cels=[0, 12, 34, 100]
    fah=[32, 65, 100, 212]

    # using regular functions
    print(list(map(Celsius2Fahrenheit, cels)))
    print(list(map(Fahrenheit2Celsius, fah)))

    # using lambda function
    print(list(map(lambda t: t*9/5 +32, cels)))
    print(list(map(lambda t: (t-32)*5/9, fah)))    

if __name__=="__main__":
    main()
