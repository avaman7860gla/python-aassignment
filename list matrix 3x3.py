l1=[[],[],[]]
l2=[[],[],[]]
l3=[[],[],[]]
for i in range(3):
    for j in range(3):
        l1[i].append(int(input()))
for i in range(3):
    for j in range(3):
        l2[i].append(int(input()))
for i in range(3):
    for j in range(3):
        l3[i].append(l1[i][j]+l2[i][j])
print(l1)
print(l2)
print(l3)
