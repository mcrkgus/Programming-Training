import sys

n = int(sys.stdin.readline())
m_list = [0]*10001

for i in range(n) :
    a = int(sys.stdin.readline())
    m_list[a] += 1
    
for i in range(10001) :
    if m_list[i] != 0 :
        for j in range(m_list[i]) :
            print(i)
