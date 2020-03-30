A,B = map(int,input().split())

ans = 0
if B / A == 1:
    ans = 1
else:
    ans = 1 + -(-(B - A) // (A - 1))
print(ans)