n=int(input("enter a number="))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(n==s):
    print("%d is a perfect number"%(n))
else:
    print("%d is not a perfect number"%(n))
