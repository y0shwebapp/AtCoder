N = input()
S,T = map(str,input().split())
ans = ''

for i in range(len(S)):
    ans += S[i]
    ans += T[i]

print(ans)