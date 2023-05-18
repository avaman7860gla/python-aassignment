s1='abc'
s2='bca'
x=len(s1)
y=len(s2)
if(x!=y):
    print("non anagram")
else:
    if(sorted(s1)==sorted(s2)):
        print("anagram")
    else:
        print("non anagram")
