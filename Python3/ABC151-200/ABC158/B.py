N, A, B = map(int, input().split())

ans = N // (A + B) * A
hasu = N % (A + B)
if hasu > A:
    ans += A
else:
    ans += hasu

print(ans)