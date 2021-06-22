def solution(name):
    answer = 0
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l = len(name)
    now = 0
    tmp = ['A'] * l
    
    
    while True:
        alpha_plus = alpha.index(name[now])
        if alpha_plus > 13:
            alpha_plus = 13 - alpha_plus % 13
        answer+=alpha_plus
        tmp[now] = name[now]
        
        if ''.join(tmp) == name:
            return answer
        
        next = 1
        while True:
            if name[(now + next) % l] != 'A' and tmp[(now + next) % l] == 'A':
                now = now + next
                break
            elif name[(now - next + l) % l] != 'A' and tmp[(now - next + l) % l] == 'A':
                now = now - next
                break
            else:
                next+=1

        answer += next
        
        
