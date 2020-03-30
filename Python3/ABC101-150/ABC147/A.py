a,b,c = map(int , input().split())

ret = "win"
if a+b+c >= 22:
    ret = "bust"
print(ret)