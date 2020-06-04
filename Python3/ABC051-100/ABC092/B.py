N = int(input())
D, X = map(int, input().split())
for i in range(N):
    t = ((D - 1) // int(input())) + 1
    X += t
print(X)