import random
grid=[]
for i in range(4):
    row=[]
    for j in range(4):
        row.append('-')
    grid.append(row)
tr=random.randint(0,3)
tc=random.randint(0,3)
while True:
    for row in grid:
        print(' '.join(row))
    try:
        ur=int(input("which row do u think im in:"))
    except ValueError:
        print("please type in a number between 0 and 3")
    uc=int(input("which column do u think im in:"))
    if tr>ur:
        print("row move up")
    elif tr<ur:
        print("row move down")
    elif tc>uc:
        print("column move up")
    elif tc<uc:
        print("column move down")
    elif tr==ur:
        print("row correct")
    elif tc==uc:
        print("column correct")
    if tr==ur and tc==uc:
        print("you got it right")
        break
