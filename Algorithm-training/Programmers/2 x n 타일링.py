def solution(n):
    a, b = 1, 2
    for _ in range(n-2):
        a, b = b, (a+b) % 1000000007
    return b
