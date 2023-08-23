# using keyword only arguments to improve code clarity

def myFunc1(arg1,arg2,*,suppressException=False):
    pass

def main():
    myFunc1(2,3,suppressException=True)


if __name__=="__main__":
    main()
