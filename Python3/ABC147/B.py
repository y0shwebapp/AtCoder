S = input()
n1 = len(S)
n2 = round(n1 / 2)

cnt = 0
for i in range(n2):
    if S[i] != S[n1 - i - 1]:
        cnt += 1

print(cnt)