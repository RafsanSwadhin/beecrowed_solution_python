A,B,C =list(map(float,input().split()))
a = 0.5*A*C
b = 3.14159*C**2
c = 0.5*(A+B)*C
d = B*B
e = A*B

	
print(f'TRIANGULO: {a:.3f}')
print(f'CIRCULO: {b:.3f}')
print(f'TRAPEZIO: {c:.3f}')
print(f'QUADRADO: {d:.3f}')
print(f'RETANGULO: {e:.3f}')

