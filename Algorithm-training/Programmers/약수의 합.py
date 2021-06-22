from math import gcd
def solution(n):
    return sum([nn for nn in range(1, n+1) if gcd(n, nn) == nn])
