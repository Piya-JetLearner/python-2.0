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