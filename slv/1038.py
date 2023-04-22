a = [4.00,4.50,5.00,2.00,1.50]

input_1 = list(map(int,input().split()))

if input_1[0] == 1:
    print(f'Total: R$ {a[0]*input_1[1]:.2f}')

elif input_1[0] == 2:
    print(f'Total: R$ {a[1]*input_1[1]:.2f}')
    

elif input_1[0] == 3:
    print(f'Total: R$ {a[2]*input_1[1]:.2f}')
    

elif input_1[0] == 4:
    print(f'Total: R$ {a[3]*input_1[1]:.2f}')
    

else:
    print(f'Total: R$ {a[4]*input_1[1]:.2f}')



