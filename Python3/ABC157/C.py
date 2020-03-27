import sys

N, M = map(int, input().split())

# N分の配列を作成
ans = []
for i in range(N):
    ans.append('')

s = 0
c = 0

ret = '-1'

# 配列に対し、入力値をセットする
for i in range(M):
    s, c = map(int, input().split())
    idx = s - 1

    if ans[idx] != '' and ans[idx] != str(c):
        print(ret)
        sys.exit(0)
    
    ans[idx] = str(c)

# 上でセットされなかった値を'0'に変換
for i in range(len(ans)):
    if ans[i] == '':
        ans[i] = '0'

if ans[len(ans) - 1] == '0':
    print('-1')
    sys.exit(0)

ret = ''.join(map(str, ans))
    
print(ret)
