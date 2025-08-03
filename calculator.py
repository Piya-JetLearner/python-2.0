print("Welcome to my calculator!")
while True:
    try:
        one=int(input("Give me your first number:"))
    except ValueError:
        print("Please enter numbers only.")
        continue
    try:
        two=int(input("enter another number:"))
    except ValueError:
        print("Please enter numbers only.")
        continue
    o=input("Enter an operator you want to use like +, -, *, /.")
    try:
        if o=="+":
            whistle=one+two
        elif o=="-":
            whistle=one-two
        elif o=="*":
            whistle=one*two
        elif o=="/":
            whistle=one/two
        else:
            raise ValueError("Invalid operator")
    except ZeroDivisionError:
        print("You cannot divide a number by zero!")
    except ValueError:
        print("Choose a valid operator.")
    print(whistle)
    e=input("do you want to exit?")
    if e=="yes":
        break
    elif e=="no":
        continue
