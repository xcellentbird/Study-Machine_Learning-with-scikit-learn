def solution(clothes):
    answer = 1
    closet = {}
    for n, k in clothes:
        if k not in closet:
            closet[k] = ['']
        closet[k].append(n)
    
    for k in closet:
        answer*=len(closet[k])
    return answer-1
