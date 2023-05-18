a=int(input("enter a="))
b=int(input("enter b="))
if(a>b):
    min=b
else:
    min=a
for i in range(1,min+1):
    if((a%i==0) and (b%i==0)):
        hcf=i
print("hcf of both number a and b=",hcf)
lcm=(a*b)/hcf
print("lcm of both number a and b=",lcm)

