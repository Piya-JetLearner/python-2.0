def c_g(c):
    return c*128
def g_c(g):
    return g/128
def te_ta(te):
    return te*0.333333
def ta_te(ta):
    return ta/0.333333

while True:
    print("Welcome to my recipe converter!")
    print("1. cups to grams")
    print("2. grams to cups" )
    print("3. teaspoon to tablespoon")
    print("4. tablespoon to teaspoon")
    print("5. Exit")
    rc=int(input("pick a number: "))
    if rc==1:
        c=int(input("how many cups do you want to convert into grams?"))
        g=c_g(c)

        print(g,'grams')
        elif rc==2:
        g=int(input("How many grams do you want to convert into cups? "))
        grams=g_c(g) 
        print(grams,'cups')
    elif rc==3:
        te=int(input("How many teaspoons do you want to convert into tablespoons? "))
        teaspoons=te_ta(te) 
        print(teaspoons,'tablespoons')
    elif rc==4:
        ta=int(input("How many tablespoons do you want to convert into teaspoons? "))
        tablespoons=ta_te(ta) 
        print(tablespoons,'teaspoons')
    elif rc==5:
        print("thank you for viewing my recipe converter! Goodbye.")
        break 
