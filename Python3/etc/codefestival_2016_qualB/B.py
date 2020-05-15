N, A, B = [int(x) for x in input().split()]
S = input()

cntA = 0
cntB = 0

for i in range(N):
    if S[i] == 'a':
        if A + B > cntA + cntB:
            cntA += 1
            print('Yes')
        else:
            print('No')
    elif S[i] == 'b':
        if A + B > cntA + cntB and B > cntB:
            cntB += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')

