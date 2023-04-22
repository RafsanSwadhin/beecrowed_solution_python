amount = int(input())
print(amount)
a=[100,50,20,10,5,2,1]
for i in a:
    print(f'{amount//i} nota(s) de R$ {i},00')
    amount= amount % i