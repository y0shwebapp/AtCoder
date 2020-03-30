N, M = [int(s) for s in input().split()]

num = 10 ** (N - 1) if N > 1 else 0
# print(num)
num_str = str(num)

char_list = []
for i in range(N):
    char_list.append(num_str[i])
# print(char_list)

flag_list = [False] * N
for _ in range(M):
    s, c = input().split()
    i = int(s) - 1

    if N > 1 and i == 0 and c == "0":
        char_list = None
        break

    if flag_list[i]:
        if char_list[i] != c:
            char_list = None
            break
    else:
        char_list[i] = c
        flag_list[i] = True

result = "-1"
if char_list is not None:
    result = "".join(char_list)
print(result)
