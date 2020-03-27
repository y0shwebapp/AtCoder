N,K = map(int, input().split())

r = 0
ans = 0
for i in range(N):
    r = K ** (i + 1)
    ans += 1
    if r >= N:
        break

print(ans)