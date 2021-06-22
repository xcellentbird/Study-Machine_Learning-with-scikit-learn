def solution(n,a,b):
    answer = 1
    while True:
        if abs(a-b) == 1 and not (a+b-3) % 4:
            return answer
        a = (a+1)//2
        b = (b+1)//2
        answer+=1
