d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400} 
li=d1.keys() 
li2=d2.keys() 
li3=[] 
for i in li: 
    if i in li2: 
        x=d1[i]+d2[i] 
        d1.update({i:x}) 
for i in li2: 
    if i not in li: 
        d1.update({i:d2[i]}) 
print(d1)
