def samzin(n):
    st = ''
    minus = 0
    while n > 0:
        nn = n%3-1-minus
        if nn < 0:
            nn = 3 + nn
            minus = 1
        else:
            minus = 0
        
        if nn == 0:
            nn = 1
        elif nn == 1:
            nn = 2
        else:
            nn = 4
        st+=str(nn)
        n = n//3        
    return st[::-1]

def solution(n):
    answer = samzin(n)
    if answer[0]=='4':
        answer = answer[1:]
    return answer
