# N = int(input())
# dic = {}
# for i in range(1, N + 1):
#     dic[i] = int(input())


# routedLst = []

# def NextRoute(i):
#     x = dic[i]
#     if x in routedLst:
#         return -1
    
#     routedLst.append(x)

#     if x == 2:
#         return len(routedLst)
#     else:
#         return NextRoute(x)

# print(NextRoute(1))

N = int(input())
lst = [int(input()) for _ in range(N)]

cnt = 0
idx = 0

while True :
    x = lst[idx]
    if x == 2:
        print(cnt)
        exit()
    cnt += 1
    idx = x - 1
    if cnt > N:
        print(-1)
        exit()