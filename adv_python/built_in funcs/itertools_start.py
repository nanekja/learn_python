import itertools

def dropFunc(x):
    if x % 2 ==0:
        return True
    return False

def main():
    
    # cycle iterator can be used to cycle over a collection
    sequence1=["Raj", "Kanthi", "Lasya"]
    cycle1=itertools.cycle(sequence1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values. Default is summation
    vals1 = [10,20,25,30,32,15,18]
    accum1=itertools.accumulate(vals1)
    print(list(accum1))

    # accumulate creates an iterator that accumulates values with max values
    vals2 = [10,20,25,30,32,15,18]
    accum2=itertools.accumulate(vals2, max)
    print(list(accum2))

    # chain connects 2 sequences together
    chain1=itertools.chain("abcd","1234")
    print(list(chain1))

    # "dropwhile" and "takewhile" will return values until a certain condition is met that stops them
    # this is similar to filter/map bulilt-in functions
    print(list(itertools.dropwhile(dropFunc, vals1)))
    print(list(itertools.takewhile(dropFunc, vals1)))






if __name__=="__main__":
    main()
