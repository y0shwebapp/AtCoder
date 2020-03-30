N, M = map(int, input().split())

# N分の配列を用意
lst = ['0'] * N

# ２桁以上の場合、左から一桁目は最小値１
if len(lst) > 1:
    lst[0] = '1'

# リストに対し、フラグ用リストを作成
lst_flg = [False] * N

for _ in range(M):
    s, c = input().split()
    i = int(s) - 1

    if lst_flg[i]:
        if lst[i] != c:
            print('-1')
            exit()
    else:
        lst[i] = c
        lst_flg[i] = True

if len(lst) > 1 and lst[0] == '0':
    print('-1')
    exit()
print(''.join(lst))