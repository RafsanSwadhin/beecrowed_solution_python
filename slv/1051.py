inn = float(input())-2000

if inn <=0:
    print("Isento")
    

elif inn <= 1000:
    tax= (inn*8)/100
    print(f"R$ {tax:.2f}")

elif inn <= 2500:
    tax = 80+ ((inn-1000)*18)/100 
    print(f"R$ {tax:.2f}")

else:
    tax = 80+ 270 + ((inn-2500)*28)/100
    print(f"R$ {tax:.2f}")
