import math

N = int(input())

ret = ':('
for i in range(50000):
    if N == math.floor(i * 1.08):
        ret = i

print(ret)