N = int(input())

cnt = 1
while True:
    if cnt * 2 > N:
        break
    cnt *= 2
print(cnt)