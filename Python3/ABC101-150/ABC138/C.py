N = int(input())
v = [int(x) for x in input().split()]

v.sort()

while True :
    x = v.pop(0)
    y = v.pop(0)
    z = (x + y) / 2
    v.insert(0, z)

    if len(v) == 1:
        print(z)
        exit()


