X = int(input())
ret = 0

ret += (X // 500) * 1000
X = X % 500
ret += (X // 5) * 5
print(ret)