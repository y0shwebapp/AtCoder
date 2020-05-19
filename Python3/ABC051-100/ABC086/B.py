import math

a, b = input().split()

x = math.sqrt(int(a + b))

ret = 'No'
if math.ceil(x) == math.floor(x):
    ret = 'Yes'
print(ret)
