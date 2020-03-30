BINGO_ROW_NO = 3

A  = []
for i in range(BINGO_ROW_NO):
    A.append(input().split())

N = int(input())


# ２次元配列検索処理
def SetBingo(A, b):
    for y in range(BINGO_ROW_NO):
        for x in range(BINGO_ROW_NO):
            if A[y][x] == b:
                A[y][x] = ''
                return 
    return 

for _ in range(N):
    b = input()
    SetBingo(A, b)

isBingo = False

# ビンゴチェック
for i in range(BINGO_ROW_NO):
    if A[i][0] == '' and A[i][1] == '' and A[i][2] == '':
        isBingo = True

for i in range(BINGO_ROW_NO):
    if A[0][i] == '' and A[1][i] == '' and A[2][i] == '':
        isBingo = True

if A[0][0] == '' and A[1][1] == '' and A[2][2] == '':
    isBingo = True

if A[0][2] == '' and A[1][1] == '' and A[2][0] == '':
    isBingo = True

if isBingo:
    print('Yes')
else:
    print('No')
