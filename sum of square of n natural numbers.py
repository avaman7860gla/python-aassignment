n=int(input("enter a number="))
sum=0
for i in range(1,n+1,1):
    x=pow(i,2)
    sum=sum+x
print("sum of square of %d natural numbers is %d"%(n,sum))
