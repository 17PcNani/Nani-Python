x = input("enter:")
sum = 0

for ch in x:
    if ch.isdigit():
        sum += int(ch)
print(sum)
