s='hello'
vl='aeiouAEIOU'
vlc=0
ctc=0
for i in s:
    if(i in vl):
        vlc+=1
    else:
        ctc+=1
print("vowels=",vlc)
print("consonant=",ctc)
