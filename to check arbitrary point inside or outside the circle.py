x1=int(input("enter absissa of center of circle="))
y1=int(input("enter ordinate of center of circle="))
r=int(input("enter radius of circle="))
x2=int(input("enter absissa of arbitrary point="))
y2=int(input("enter ordinate of arbitrary point="))
a=pow(x1-x2,2)+pow(y1-y2,2)
d=pow(a,0.5)
if(d==r):
    print("arbitrary point located on the circle")
elif(d>r):
    print("arbitrary point located outside the circle")
else:
    print("arbitrary point located inside the circle")
