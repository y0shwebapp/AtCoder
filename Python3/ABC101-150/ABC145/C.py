from statistics import mean

def cal(x1 , y1 , x2 , y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))**0.5

n=int(input())

lst = list()
for i1 in range(n):
    lst.append(input())

ansLst=list()
tmpLst=list()
for i2 in range(n):
    x1 , y1 = map(int , lst[i2].split())
    for i3 in range(n):
        if i2 == i3:
            continue
        else:
            x2 , y2 = map(int , lst[i3].split())
            tmpLst.append(cal(x1 , x2 , y1 , y2))
    ansLst.append(sum(tmpLst))
print(mean(ansLst))
