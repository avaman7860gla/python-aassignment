n=int(input("enter a number="))
x=n
sum=0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+(r*r*r)
if(sum==x):
    print("%d is armstrong number"%(x))
else:
    print("%d is not a armstrong number"%(x))
