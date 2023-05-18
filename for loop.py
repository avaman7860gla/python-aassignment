k=input("1.counting\n2.odd series\n3.even series\nenter=")
if(k=='1'):
    x=int(input("enter starting point="))
    y=int(input("enter end point="))
    z=int(input("enter updation="))
    w=input("a.Print Vertically\nb.Print Horizontally\nenter=")
    if(w=='a'):
        for i in range(x,y+1,z):
            print(i)
    elif(w=='b'):
        for i in range(x,y+1,z):
            print(i,end=' ')
    else:
        print("invalid input")
elif(k=='2'):
    x=int(input("enter starting point="))
    y=int(input("enter end point="))
    z=int(input("enter updation="))
    w=input("a.Print Vertically\nb.Print Horizontally\nenter=")
    if(w=='a'):
        if(x%2!=0):
            for i in range(x,y+1,2):
                print(i)
        else:
            for i in range(x+1,y+1,2):
                print(i)
    elif(w=='b'):
        if(x%2!=0):
            for i in range(x,y+1,2):
                print(i,end=' ')
        else:
            for i in range(x+1,y+1,2):
                print(i,end=' ')
    else:
        print("invalid input")
elif(k=='3'):
    x=int(input("enter starting point="))
    y=int(input("enter end point="))
    z=int(input("enter updation="))
    w=input("a.Print Vertically\nb.Print Horizontally\nenter=")
    if(w=='a'):
        if(x%2==0):
            for i in range(x,y+1,2):
                print(i)
        else:
            for i in range(x+1,y+1,2):
                print(i)
    elif(w=='b'):
        if(x%2==0):
            for i in range(x,y+1,2):
                print(i,end=' ')
        else:
            for i in range(x+1,y+1,2):
                print(i,end=' ')
    else:
        print("invalid input")
else:
    print("invalid input")
