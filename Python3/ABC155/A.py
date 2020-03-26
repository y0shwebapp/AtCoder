A,B,C = map(str , input().split())

ret = "No"

if A == B and A != C:
    ret = "Yes"
elif A == C and A != B:
    ret = "Yes"
elif B == C and B != A:
    ret = "Yes"

print(ret)