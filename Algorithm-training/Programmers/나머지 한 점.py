def solution(v):
    answer = v[2][:]
    for i in range(2):
        if v[2][0] == v[i][0]:
            answer[0] = v[1-i][0]
        if v[2][1] == v[i][1]:
            answer[1] = v[1-i][1]
    return answer
