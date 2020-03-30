n=int(input())

ret = 'No'
for x in range(1,10):
    for y in range(1,10):
        if x*y == n:
            ret = 'Yes'
            break

print(ret)