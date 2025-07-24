from datetime import datetime
while True:
    print("Welcome to the journal app")
    print("press 1 to add entries, press 2 to view entries, press 3 to exit")
    choice=int(input("tell us your choice: "))
    if choice==1:
        file = open("journal.txt","a")
        user=input("what do you want to add in your journal?")
        date=datetime.now().strftime("%Y-%m-%d")
        file.write("\n"+date +" "+user)
    elif choice==2:
        file = open("journal.txt","r")
        content = file.read()
        print(content)
    elif choice==3:
        print("thank you for using this app")
        break
        