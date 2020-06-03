X = int(input())

def isSosu(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x - 1, 2):
        if x % i == 0:
            return False
    return True

while True:
    if isSosu(X):
        print(X)
        break
    X += 1