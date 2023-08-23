#

import collections
import string

def main():

    # Initialize a deque with lowercase letters
    d=collections.deque(string.ascii_lowercase)

    # to check length of the deque
    print(str(len(d)))

    # deques can be iterated over
    for ele in d:
        print(ele.upper(), end=",")

    # manipulate items on either side of the deque
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    d.rotate(10)
    print(d)



if __name__=="__main__":
    main()