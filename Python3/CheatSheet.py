

# 入力
a1=input()                      # input='abc'  a1='abc'
a2=list(input())                # input='abc'  a2=['a','b','c']
a3=int(input())                 # input='5'    a3=5
a4,a5=map(int,input().split())  # input='1 2'  a4=1,a5=2
a6=[int(x) for x in input().split()]   # input='4 5'   a6=20

# 出力
s1='hoge'
print(s1)                        # s='hoge'  output='hoge\n'
s2=2
s3=5
print(str(s2/s3)+'です。')      # s1=2 s2=5 output='0.4です。'

# 小数点
c = 0.364364
print(c) #0.364364
print("{:.6f}".format(c))       #0.364364
print("{:.4f}".format(c))       #0.3644 小数点第4位に丸めることもできる。

a=10
b=3
print(a/b)                      # 3.3333333333333335 （除算）
print(a%b)                      # 1 （余り）
print(a//b)                     # 3 （切り捨て除算）
print(-(-a//b))                 # 4 （切り上げ除算）

d = 810
print("{:b}".format(d))         #1100101010  2進数表記 
print("{:o}".format(d))         #1452        8進数表記
print("{:x}".format(d))         #32a         16進数小文字表記
print("{:X}".format(d))         #32A         16進数大文字表記

# ゼロ埋め・幅寄せ
print("python".ljust(15,'-')) # 左詰め
#python---------
print("python".center(15,'-'))# 中央寄せ
#-----python----
print("python".rjust(15,'-')) # 右詰め
#---------python
print(str(29).rjust(10,'0')) #10桁ゼロ埋め
#0000000029

# ２分探索

# 巨大なリストに存在する0以下の数字をすべて簡単に消す必要があるとき
import bisect
listA=[1,2,5,2,4,6,7,8,6,56,3,56,76,34,32,2,6,0,32,6,0] 
listA.sort()
zeroindex=bisect.bisect_right(listA,0)  #ソートされたリスト内で0の場所を探し、右側Indexを返す
clearlistA=listA[zeroindex:]            #0以下が存在しないリストを得る

# 文字列操作
'abc123def'[:]      #すべての文字列が取れる             #'abc123def'
'abc123def'[-1:]    #終端文字がとれる                   #'f'
'abc123def'[:-1]    #最後の1文字以外のものがとれる。    #'abc123de'
'abc123def'[::-1]   #文字が逆転する                     #'fed321cba'

# 正規表現
import re
s='hoge6hoge21foo:bar'
re.findall(r'[a-z]+',s) #['hoge', 'hoge', 'foo', 'bar']
re.findall(r'[a-z0-9]+',s) # ['hoge6hoge21foo', 'bar']

# import関連

# AAA.py
# def func():
import AAA              # モジュール[AAA]を呼び出す
AAA.func()

import AAA as A         # モジュール[AAA]を呼び出し、別名を付ける[A]
A.func()                # 別名で呼べる

from AAA import func    # モジュールの[func()]のみを呼び出す
func()                  # モジュール名無しで呼び出せる