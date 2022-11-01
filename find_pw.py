#비밀번호 찾기 
# input : 정보 , 찾고 싶은 내용
# output : 찾은 내용
import sys
a, b = map(int, sys.stdin.readline().split())
info = {}
find = []
res = []
for i in range(a) :
    site, pw = sys.stdin.readline().split()
    info[site] = pw

for _ in range(b) :
    f = sys.stdin.readline().rstrip()
    print(info[f])
