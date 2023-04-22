A,B,C = list(map(float,input().split()))

math = B**2 - 4*A*C


if A ==0 or math< 0:
    print('Impossivel calcular')

else:
    r1= (-B+(math)**0.5)/(2*A) # ai line ta if er age dele zerodivission error 
                               # hobe
    r2= (-B-(math)**0.5)/(2*A)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
   