from collections import deque
def nzin(n, num):
    alpha = ['A','B','C','D','E','F']
    ret = deque()
    
    if num == 0:
        return '0'
    
    while num != 0:
        ap = str(num % n)
        if int(ap) >= 10:
            ap = alpha[int(ap)-10]
        ret.appendleft(ap)
        num = num // n

    return ''.join(ret)

def solution(n, t, m, p):
    answer = ''
    say = ''
    num = 0
    while len(say) < t * m:
        say += nzin(n, num)
        num += 1
    
    for i in range(p-1, t*m, m):
        answer += say[i]
        
    return answer
