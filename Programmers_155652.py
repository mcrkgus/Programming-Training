def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for i in skip :
        if i in alpha : 
            alpha = alpha.replace(i, "")
    for j in s :
        res.append(alpha[(alpha.index(j)+index) % len(alpha)])
    return "".join(res)
    
   
