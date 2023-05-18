di={} 
n=int(input("enter the range: ")) 
for i in range(1,n+1): 
    x=i*i 
    di.update({i:x}) 
print(di) 
