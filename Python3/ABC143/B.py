n=int(input())
d=[int(x) for x in input().split()]

sum=0
for i in range(n-1):
    for j in range(i+1,n):
        sum = sum + d[i] * d[j]
print(sum)