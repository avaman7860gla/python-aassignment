bs=float(input("enter base salary="))
if(bs>20000):
    hra=(bs*30)/100
    da=(bs*95)/100
elif(bs<=20000 and bs>10000):
    hra=(bs*25)/100
    da=(bs*90)/100
elif(bs<=10000):
    hra=(bs*20)/100
    da=(bs*80)/100
gross=bs+hra+da
print("gross salary=",gross)
