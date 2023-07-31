n = int(input())
m_list = []
for i in range(n) :
    a = int(input())
    m_list.append(a)
    
m_list.sort()
print(*m_list, sep='\n')
