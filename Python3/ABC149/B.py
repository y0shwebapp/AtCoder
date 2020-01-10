A,B,K = map(int , input().split())
if A >= K:
    A = A - K
else:
    B = B + A - K
    A = 0
    if B < 0:
        B = 0
print(str(A) + ' ' + str(B))