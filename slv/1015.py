"""
xy = list(map(float,input().split()))
xy2 = list(map(float,input().split()))
x1 = xy[0]
x2 = xy2[0]
y1 = xy[1]
y2 = xy2[1]

result = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f'{result:.4f}')

"""

'''
x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))

result = ((x2-x1)**2 + (y2-y1)**2)**0.5
c
'''

import math

x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))

result = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

print(f'{result:.4f}')