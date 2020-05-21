n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))



b = 1
s = 0
move = []

while True :
    move.append(b)
    b = a[b - 1]
    s += 1
    if b == 2 :
        print(s)
        exit(0)
    if n < s :
        print(-1)
        exit(0)
