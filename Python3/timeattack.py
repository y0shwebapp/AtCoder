import time

start_time = time.time()

def func(beki):
    ret = 0
    for i in range(10**beki):
        ret += 1
    return ret

ret = func(6)

print(ret)

proc_time = time.time() - start_time

print("処理時間：" + str(proc_time))