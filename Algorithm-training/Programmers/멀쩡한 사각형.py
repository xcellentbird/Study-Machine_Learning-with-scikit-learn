from math import gcd
def solution(w,h):
    answer = 1
    _gcd = gcd(w,h)
    _w = int(w/_gcd)
    _h = int(h/_gcd)
    wh = 0
    fx = lambda x: (h/w)*x
    if w == 1 or h == 1:
        return 0
    for x in range(_w-1,0,-1):
        wh += int(fx(x))*2
    answer = w * h -((_w * _h) - wh)*_gcd
    return answer
