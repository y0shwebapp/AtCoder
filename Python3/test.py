N = int(input())

def calc(x):
    if x % 3 == 0:
        return True
    for i in str(x):
        if i == '3':
            return True
    return False

ret = []
for i in range(1, N+ 1):
    if calc(i):
        ret.append(i)

ret2 = ''
for r in ret:
    ret2 = ret2 + ' ' + str(r)
print(ret2)