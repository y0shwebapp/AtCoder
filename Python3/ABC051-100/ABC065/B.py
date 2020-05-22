N = int(input())
dic = {}

isFirst = True
for i in range(1, N + 1):
    # dic[i] = int(input())
    if isFirst:
        dic[i] = N
        isFirst= False
    else:
        dic[i] = i - 1


routedLst = []

def NextRoute(i):
    x = dic[i]
    if x in routedLst:
        return -1
    
    routedLst.append(x)

    if x == 2:
        return len(routedLst)
    else:
        return NextRoute(x)

print(NextRoute(1))
