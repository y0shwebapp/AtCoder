import itertools

N = int(input())
P = input().replace(' ','')
Q = input().replace(' ','')

item = []
for i in range(1,N + 1):
    item.append(str(i))
lst = list(itertools.permutations(item))

item2 = []
for l in lst:
    item2.append(''.join(l))

a = abs(item2.index(P) - item2.index(Q))
print(a)
