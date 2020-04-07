import math

A, B = map(int, input().split())

tmp = B * 10
for i in range(tmp, tmp + 10):
    if math.floor(i * 0.08) == A:
        print(i)
        exit()
print(-1) 
