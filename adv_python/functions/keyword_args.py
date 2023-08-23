# variable Keyword arguments

def concatenate(**kwargs):
    result=''
    for arg in kwargs.values():
        result+=arg
    return result

def main():
    print(concatenate(a="Apple",b="Ber"))

if __name__=="__main__":
    main()
