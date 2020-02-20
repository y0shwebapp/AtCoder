a,b = map(int,input().split())

a1 = ''
b1 = ''

for i in range(b):
    a1 = a1 + str(a)
for i in range(a):
    b1 = b1 + str(b)

if a1 < b1:
    print(a1)
else:
    print(b1)