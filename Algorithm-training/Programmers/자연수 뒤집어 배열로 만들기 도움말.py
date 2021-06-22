def solution(n):
    answer = []
    for nn in str(n)[::-1]:
        answer.append(int(nn))
    return answer
