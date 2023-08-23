# Demonstrate the use of variable argument lists

def addition(*args):
    result=0
    for arg in args:
        result+=arg
    return result

def main():
    print(addition(3,4,9))

    list1=[45,2,37,434,1,43]
    print(addition(*list1))

if __name__=="__main__":
    main()