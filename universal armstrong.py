n=int(input("enter a number="))
x=n
p=len(str(n))
sum=0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r**p
if(sum==x):
    print("%d is armstrong"%(x))
else:
    print("%d is not armstrong"%(x))
