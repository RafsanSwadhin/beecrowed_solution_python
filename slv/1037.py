nana = float(input())

if nana >= 0 and nana<= 25.0000:
    print("Intervalo [0,25]")

elif nana >= 25.00001 and nana <= 50.0000000:
    print("Intervalo (25,50]")

elif nana >= 75.00001 and nana <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")