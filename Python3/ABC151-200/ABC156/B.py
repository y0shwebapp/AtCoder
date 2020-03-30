
# xをn進数に変換
def To_Base_number(x, n):
    ret = []
    while x > 0:
        ret.insert(0, x % n)
        x = x // n
    return ''.join(map(str, ret))


N,K = map(int, input().split())
print(len(To_Base_number(N, K)))

