import sys

N = int(input())
X = [int(x) for x in input().split()]

ret = sys.maxsize

for i in range(min(X) , max(X) + 1):
    pow = 0
    for x in X:
        pow += (x - i) ** 2
    if pow < ret:
        ret = pow

print(ret)