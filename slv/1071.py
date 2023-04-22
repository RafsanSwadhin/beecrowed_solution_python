
in1 = 6 #int(input())
in2 =  -5   #int(input())
sum = 0
for num in range (in2, in1):
    if num % 2 != 0:
        
        print(num)
        sum = sum+num
print(sum)

'''
sum_odd = 0
for num in range(-6, 6):
    if num % 2 != 0:
        sum_odd += num

print("The sum of odd numbers between -6 and 5 is:", sum_odd)
'''
