str1=input("Enter first string:")
str2=input("Enter second string")
count1=0
count2=0
for i in str1:
    count1+=1
    temp1=count1
for i in str2:
    count2+=1
    temp2=count2
if temp1>temp2:
    print("str1 is larger")
else:
    print("str2 is larger")
    
