# Use iterator functions like enumerate, zip, iter, next

def main():

    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(i)
    print(next(i))
    print(next(i))

    # iterate using a function and a sentinel. Here '' is the sentinal where the iter will stop when it reaches empty/EOF
    with open("/home/nanekja/python_ex/adv_python/testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # Regular iteration over the days list
    for i in days:
        print(i)

    # To generate index for each day of days list
    for i in range(len(days)):
        print(i+1, days[i])

    # Enumerate reduces code and provides counter
    for i,m in enumerate(days, start=1):
        print(i,m)

    # iterating multiple sequences at same time; zip combines sequences
    for i in zip(days, daysFr):
        print(i)

    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")

if __name__=="__main__":
    main()