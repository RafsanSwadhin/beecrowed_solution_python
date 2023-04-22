N1,N2,N3,N4 = list(map(float,input().split()))

avg = (N1+N2+N3+N4)/4
print(f'Media: {avg:.1f}')

if avg == 7 or avg >= 7:
    print("Aluno aprovado")

elif avg < 5:
    print("Aluno reprovado")

elif avg >= 5 and avg <= 6.9:
    print("Aluno em exame")

N5 = float(input())
print(f'Nota do exame: {N5:.1f}')

sum = (N5+avg)/2
if sum >= 5 :
    print('Aluno aprovado')
elif sum <= 4.9:
    print('Aluno reprovado')

avg1 = (avg+N5)/2

print(f'Media final: {avg1:.1f}')