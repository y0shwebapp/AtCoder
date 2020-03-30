H,N = map(int , input().split())
A = input().split()

for a in A:
    H -= int(a)

if H <= 0:
    print('Yes')
else:
    print('No')