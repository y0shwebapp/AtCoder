K, N = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

lst = []
for n in range(N):
    if n + 1 != N:
        lst.append(A[n+1] - A[n])
    else:
        lst.append(K - A[n] + A[0])

print(K - max(lst))
