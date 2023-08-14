#arrList에 1월부터 12월까지 일수를 넣어준다. 
#입력 받은 월의 직전 월까지 일수를 계산하기 위해 Day에 arrList값을 더한다. 
#해당 월의 일 수를 for문을 나와서 더해주고 7로 나눈 나머지를 넣어준다. 그리고 weekList에서 그 값에 해당하는 요일을 출력하게 한다. 
x, y = map(int, input().split())
Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]


for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7
 
print(weekList[Day])
