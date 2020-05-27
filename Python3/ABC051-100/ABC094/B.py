N, M, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

cnt_a = len([x for x in A if x < X])
cnt_b = len([x for x in A if x >= X])

print(min(cnt_a, cnt_b))