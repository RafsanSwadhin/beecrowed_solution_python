'''
def num():
    N= int(input())
    for i in range(1,N):
        n = int(input())
        if n == 0:
            return("NULL")
        elif n %2 == 0 and n < 0:
            return("EVEN POSITIVE")
        elif n %2 == 0 and n > 0:
            return("EVEN NEGATIVE")
        elif n%2 != 0 and n > 0:
            return("ODD POSITIVE")
        else :
            return("ODD NEGATIVE ")
print(num())
'''

def num():
    N = int(input())
    results = []  # Store the results for each input number
    for i in range(N):
        
        n = int(input())
        if n == 0:
            results.append("NULL")
        elif n % 2 == 0 and n > 0:
            results.append("EVEN POSITIVE")
        elif n % 2 == 0 and n < 0:
            results.append("EVEN NEGATIVE")
        elif n % 2 != 0 and n > 0:
            results.append("ODD POSITIVE")
        else:
            results.append("ODD NEGATIVE")
    return results

print("\n".join(num()))
