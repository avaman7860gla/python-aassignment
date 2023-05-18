a=int(input("enter first side of triangle="))
b=int(input("enter second side of triangle="))
c=int(input("enter third side of triangle="))
if(a+b+c==180):
    if(a==b & b==c & a==c):
        print("equilateral triangle")
    elif(a==b | b==c | a==c):
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("invalid sides of triangle")
