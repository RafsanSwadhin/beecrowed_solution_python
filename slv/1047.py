a,b,c,d = list(map(int,input().split()))

start = a*60+b
end = c*60 +d

dif = end - start

if dif <= 0 :
    dif = dif+24*60

hour = dif // 60
min = dif % 60

print(f'O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)')