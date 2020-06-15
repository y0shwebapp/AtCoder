N = input()
A = [int(x) for x in input().split()]


def calc(A):
    for i in range(len(A)):
        if A[i] == 0:
            return False
        if A[i] % 2 == 1:
            return False
        A[i] = A[i] // 2
    return True

cnt = 0
while True:
    if calc(A) == False:
        break
    cnt += 1
print(cnt)