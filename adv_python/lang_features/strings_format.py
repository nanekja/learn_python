# There are 4 ways to format strings

from string import Template

def main():
    # 1) Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python","Joe")
    print(str1)

    # 2) Template strings
    templ = Template("You're watching ${title} by ${author}")
    str2 = templ.substitute(title="Advanced Python", author="Joe")
    print(str2)

    # 3) Substitute with Dictionary
    data = {
        "author" : "Joe",
        "title" : "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)


if __name__=="__main__":
    main()