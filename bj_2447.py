K = int(input())
area = []
height = []
width = []
empty = []
#가장 긴 가로변과 세로변의 길이와 인덱스를 0으로 초기화함

for i in range(6) :
    direction, distance = map(int, input().split())
    area.append([direction, distance])
    if area[i][0] == 3 or area[i][0] == 4 :
        height.append(area[i][1])
    if area[i][0] == 1 or area[i][0] == 2 :
        width.append(area[i][1])

for i in range(6) :
    if area[i][0] == area[(i+2)%6][0] :
        empty.append(area[(i+1)%6][1])

total_area = max(height) * max(width)
empty_area = empty[0] * empty[1]
print((total_area-empty_area)*K)
