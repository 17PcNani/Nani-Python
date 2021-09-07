s1=input("enter first string:")
s2=input("enter second string:")
status=0
if len(s1)==len(s2):
    for ch in s1:
        if ch in s2:
            status+=1
            continue
        else:
            print("its not a anagram")
else:
    print("its not a anagram")
if status==len(s1):
    print("It is a anagram")
        
        
