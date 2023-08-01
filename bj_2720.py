T = int(input())

for _ in range(T) :
    a = int(input())
    quarter_cnt = a // 25
    a = a - (25*quarter_cnt)
    
    dime_cnt = a // 10
    a = a - (10*dime_cnt)
    
    nickel_cnt = a // 5
    a = a - (5*nickel_cnt)
    
    penny_cnt = a
    
    print(quarter_cnt, dime_cnt, nickel_cnt, penny_cnt)
