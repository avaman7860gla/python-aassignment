n=input()
c=len(n)
s=0
for i in n:
    s=s+int(i)**c
if(str(s)==n):
    print("armstrong")
else:
    print("not armstrong")
