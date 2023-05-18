di={"1": 10, "2": 20, "3": 30, "4": 40, "5": 50,"f":60} 
keyy=input("enter the key u wanna find: ") 
x=len(di) 
count=0 
li=di.keys() 
for i in li: 
    if i==keyy: 
        count+=1 
if count==1: 
    print("key already exists") 
else: 
    print("key dont exists") 
