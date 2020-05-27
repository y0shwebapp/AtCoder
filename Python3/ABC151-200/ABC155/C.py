dic = {}
for i in range(int(input())):
    s = input()
    if s in dic:
        dic[s] = dic[s] + 1
    else:
        dic[s] = 1
max_v = max(dic.values())
ret = [k for k, v in dic.items() if v == max_v]

ret.sort()
print('\n'.join(ret))