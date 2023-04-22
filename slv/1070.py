
#solution 1

inn = int(input())
#print(inn)
#ja = inn+1
#print(ja)

if inn%2 ==0:
    for i in range(inn+1,inn+12,2):
        print(i)

elif inn%2 ==1:
    for j in range(inn,inn+12,2):
        print(j)
#for i in range(inn,inn+13,2):
    #print(i)