N, M, C = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    A = [int(x) for x in input().split()]
    sum = 0
    for j in range(M):
        sum += A[j] * B[j] 
    if sum + C > 0:
        ans += 1

print(ans)
