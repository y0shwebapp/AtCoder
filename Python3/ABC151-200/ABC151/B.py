N,K,M = map(int , input().split())
A = input().split()
sm = 0

for a in A:
    sm += int(a)

ans = N * M - sm

if ans < 0:
    ans = 0

if ans > K:
    print(-1)
else:
    print(ans)