N, M = map(int, input().split())
A = [int(x) for x in input().split()]

for a in A:
    N -= a

if N < 0:
    N = -1

print(N)