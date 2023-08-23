# Demo of built-in functions

def main():
    list1 = [1,2,3,5,0,8]

    # any() will return true if any of the sequence values are true
    print(any(list1))

    # all() will return true only if all values are true. In the following case we will get false as one of the element is 0
    print(all(list1))

    # min() and max() will return minimum and maximum values
    print(min(list1))
    print(max(list1))

    # sum() will sum up all values
    print(sum(list1))


if __name__=="__main__":
    main()
