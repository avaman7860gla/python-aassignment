a=float(input("enter amount of shipping="))
if(a>25000):
    print("Category=Gold")
    print("@you got 20% discount!!")
    total=a-((20*a)/100)
    print("amount=",total)
elif(a>10000 and a<25000):
    print("Category=Silver")
    print("@you got 10% discount!!")
    total=a-((10*a)/100)
    print("amount=",total)
elif(a<10000):
    print("Category=Bronze")
    print("@you got 5% discount!!")
    total=a-((5*a)/100)
    print("amount=",total)
