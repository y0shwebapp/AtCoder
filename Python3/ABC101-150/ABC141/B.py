S=input()
oddLst=['R','U','D']
evenLst=['L','U','D']

ret='Yes'
cnt=0
for s in S:
    cnt+=1
    if(cnt%2):
        if s not in oddLst:
            ret='No'
    else:
        if s not in evenLst:
            ret='No'

print(ret)
