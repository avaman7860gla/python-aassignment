a=float(input("enter physics marks out of 100="))
b=float(input("enter chemistry marks out of 100="))
c=float(input("enter biology marks out of 100="))
d=float(input("enter mathematics marks out of 100="))
e=float(input("enter computer marks out of 100="))
per=(a+b+c+d+e)/5
print("percentage=",per)
if(per>=90):
    print("grade=A")
elif(per>=80 and per<90):
    print("grade=B")
elif(per>=70 and per<80):
    print("grade=C")
elif(per>=60 and per<70):
    print("grade=D")
elif(per>=40 and per<60):
    print("grade=E")
elif(per<40):
    print("grade=F")
