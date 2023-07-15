N = int(input())
word_list = []


for i in range(N) :
    word_list.append(input())
    
set_word_list = set(word_list)	
word_list = list(set_word_list)
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)
