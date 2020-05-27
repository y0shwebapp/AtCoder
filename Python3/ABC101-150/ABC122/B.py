S = input()
targetLst = ['A' , 'C', 'G', 'T']

ansLst = []

for i in range(len(S)):
    tmp = []
    for j in range(i, len(S)):
        if S[j] in targetLst:
            tmp.append(S[j])
        else:
            break
    ansLst.append(len(tmp))

ansLst.sort()
ansLst.reverse()

print(ansLst[0])