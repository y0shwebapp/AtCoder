N = input()
A = [int(x) for x in input().split()]

ans = 'APPROVED'
for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ans = 'DENIED'
            break

print(ans)

