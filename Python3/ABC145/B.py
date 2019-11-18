S=int(input())
N=input()
if S%2:
    print('No')
else:
    splitLen=int(S/2)
    if N[:splitLen] == N[splitLen:]:
        print('Yes')
    else:
        print('No')