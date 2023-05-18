n=int(input("enter number="))
s=0
while(n>0):
    r=n%10
    n=n//10
    s=s+r
print("sum of each digits=",s)
