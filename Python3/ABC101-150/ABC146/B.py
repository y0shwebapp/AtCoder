N = int(input())
S = input()
dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
       'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,
       'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,
       'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,
       'Y':24,'Z':25}

res = ''
for s in S:
    idx = (dic[s]+N) % 26
    keys = [k for k, v in dic.items() if v == idx]
    res += keys[0]


print(res)