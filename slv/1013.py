'''
list = [11,22,56]
print(list[0])
print(max(list))

a = list(map(int,input().split()))

#7 14 106
#print(a)
#print(max(a))

if a[0] > a[1]:
    if a[0] > a[2]:
        print(f'{a[0]} eh o maior')
    else:
        print(f'{a[2]} eh o maior')

elif a[1] > a[2]:
    print(f'{a[2]} eh o maior')
   
else :
     print(f'{a[2]} eh o maior')

'''
a = list(map(int,input().split()))

print(f'{max(a)} eh o maior')







