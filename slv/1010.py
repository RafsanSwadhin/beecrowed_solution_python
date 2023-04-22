a = input().split(' ')[1:]
b = input().split(' ')[1:]

t1 = int(a[0])*float(a[1]) #a[0] dewar karon holo list e ekhn 2 ta items ache
t2 = int(b[0])*float(b[1])
total = t1+t2

print(f'VALOR A PAGAR: R$ {total :.2f}')

a = input().split()