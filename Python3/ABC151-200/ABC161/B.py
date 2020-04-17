N, M = map(int, input().split())
A = [float(x) for x in input().split()]

A.sort(reverse=True)

sum = 0.0
for a in A:
    sum += a

ret = 'Yes'
for i in range(M):
    if (A[i] < (sum / (4 * M))):
        ret = 'No'
        break

print(ret)

