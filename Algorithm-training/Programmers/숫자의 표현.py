def solution(n):
    answer = 0
    for n_start in range(1, n+1):
        for n_end in range(n_start+1, n+2):
            s = sum(range(n_start, n_end))
            if s >= n:
                if s == n:
                    answer+=1
                break
    return answer
