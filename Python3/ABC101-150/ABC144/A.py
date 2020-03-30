n=[int(x) for x in input().split()]

ans = -1
if n[0]>9:
    print(-1)
elif n[1]>9:
    print(-1)
else:
    print(n[0]*n[1])