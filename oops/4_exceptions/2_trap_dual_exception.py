import sys

try:
    arg=sys.argv[1]
    num=int(arg)

except (IndexError, ValueError):
    exit("please enter an integer on command line")

print("Thanks for the integer")

