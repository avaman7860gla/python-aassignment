x=input("enter any character=")
if((x>='A' and x<='Z') or (x>='a' and x<='z')):
    print("alphabet")
elif(x>='0' and x<='9'):
    print("digits")
else:
    print("special character")
