n,k = map(int,input().split())
h = [int(x) for x in input().split()]

cnt = 0
for i in h:
    if i >= k:
        cnt = cnt + 1

print(cnt)
