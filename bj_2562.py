number = []
for i in range(9) :
    num = int(input())
    number.append(num)
    
max_num = max(number)
idx = number.index(max_num) + 1
print(max_num)
print(idx)
