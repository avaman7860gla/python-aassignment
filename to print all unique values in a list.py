li=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}] 
l2=[] 
l3=[] 
for i in li: 
    l2.extend(i.values()) 
for i in l2: 
    if i not in l3: 
        l3.append(i) 
print(l3) 
