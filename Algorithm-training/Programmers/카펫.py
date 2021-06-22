def solution(brown, red):
    n = brown+red
    for i in range(1,n+1):
        # brown + red = x * y, (x-2) * (y-2) = red
        if not n%i and (i-2) * (n//i - 2) == red:
            return sorted([i, n//i], reverse=True)
