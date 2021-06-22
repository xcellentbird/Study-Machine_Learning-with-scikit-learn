from math import factorial
def solution(n, k):
    answer = []
    arr = list(range(1, n+1))
    while n > 0:
        remain = k % factorial(n-1)
        quotient = k // factorial(n-1)
        if not remain:
            quotient -= 1
        answer.append(arr.pop(quotient))
        
        k = remain
        n -= 1
    return answer
