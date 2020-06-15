import math
import decimal

A, B = [decimal.Decimal(x) for x in input().split()]
print(math.floor(A * B))
