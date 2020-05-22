N = int(input())
A = [int(x) for x in input().split()]

dct = {}
for i in range(N):
    dct[i + 1] = A[i]

lst = []
for k, v in sorted(dct.items(), key=lambda x: x[1]):
    lst.append(str(k))

print(' '.join(lst))