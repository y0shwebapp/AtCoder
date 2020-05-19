N = int(input())
d = [int(x) for x in input().split()]

d.sort()
x = int(N / 2)

print(d[x] - d[x - 1])