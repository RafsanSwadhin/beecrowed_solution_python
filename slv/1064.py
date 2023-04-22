list = []
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
list.append(num6)
#print(list)
#print(type(list))
#print(type(list[2]))

#list = [int(num) if num.isnumeric() else float(num) for num in list]
print(type(list[0]))
a = []
for i in list: 
	if i > 0:
		
		a.append(i)
		#print(a)
#print(a)
lenn = len(a)
print(lenn)
print(f'{lenn} valores positivos')
a_sum = sum(a)
print(f"{a_sum/lenn:.1f}")
#print(type(a))
#print(type(a[0]))
