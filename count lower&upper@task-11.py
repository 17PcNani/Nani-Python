s1=input("Enter a string:")
count1=0
count2=0
for i in s1:
    if(i.islower()==True):
        count1+=1
    if(i.isupper()==True):
        count2+=1
print("The no of lowercase latters are:",count1)
print("The no of uppercase letters are:",count2)
