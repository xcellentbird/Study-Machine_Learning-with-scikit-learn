def solution(n):
    if n in [1,2,3]:
        return n
    f1, f2 = 2, 3
    for _ in range(n-3):
        f1, f2 = f2, (f1+f2) % 1234567
    return f2
