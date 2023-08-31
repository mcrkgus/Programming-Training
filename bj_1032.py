N = int(input())
file_name = list(input())
for i in range(N-1) :
    next_file = list(input())
    for j in range(len(file_name)) :
        if file_name[j] != next_file[j] :
            file_name[j] = '?'
            


print(''.join(file_name))
