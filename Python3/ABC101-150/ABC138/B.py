N = int(input())
A = [int(x) for x in input().split()]

A1 = 0

for i in A:
    A1 += 1 / i

print(1 / A1)