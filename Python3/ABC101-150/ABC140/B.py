N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

prevIdx = -99
ret = 0
for a in A:
    a -= 1
    ret += B[a]
    if a == prevIdx + 1:
        ret += C[a - 1]
    prevIdx = a
print(ret)