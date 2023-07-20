n = int(input())
stack = []
ans = []
k = 1
flag = 0
for _ in range(n) :
    num = int(input())
    while k <= num :
        stack.append(k)
        ans.append("+")
        k += 1
    if stack[-1] == num :
        stack.pop()
        ans.append("-")
    else : 
        flag = 1
        break
     
if flag == 0 :
    for i in ans : 
        print(i)
else :
    print("NO")
