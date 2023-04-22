age = []
while True:
    num = int(input())

    if num <0:
        break
    else:
        age.append(num)

#print(age)
lenn = len(age)
ages = sum(age)
avg = ages/lenn
print(f"{avg:.2f}")