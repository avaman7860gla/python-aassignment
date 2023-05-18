n=int(input("enter any number="))
c=0
for i in range(1,n):
    if(n%i==0):
        c+=1
if(c>=2):
    print("not prime")
else:
    print("prime")
