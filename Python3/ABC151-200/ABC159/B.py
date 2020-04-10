S = input()

def Check1(S):
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - 1 - i]:
            return False
    return True

def Check2(S):
    S2 = ""
    for i in range(0, (len(S) - 1) // 2):
        S2 = S2 + S[i]
    return Check1(S2)

def Check3(S):
    S3 = ""
    for i in range((len(S) + 3) // 2 - 1, len(S)):
        S3 = S3 + S[i]
    return Check1(S3)

if Check1(S) and Check2(S) and Check3(S):
    print("Yes")
else:
    print("No")