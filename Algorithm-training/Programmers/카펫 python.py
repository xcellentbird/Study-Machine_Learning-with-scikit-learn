def solution(brown, yellow):
    answer = []
    wh = []
    bb = int((brown+4)/2)
    for i in range(1,int(bb/2)+1):
        if (bb-i-2) * (i-2) == yellow:
            answer = [bb-i, i]
        
    return answer
