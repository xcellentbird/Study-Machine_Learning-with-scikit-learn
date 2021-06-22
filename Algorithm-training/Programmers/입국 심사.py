def solution(n, times):
    times.sort()
    _max = min(times) * n
    _min = 0
    
    while True:
        i = (_max + _min) // 2
        hap = 0
        for t in times:
            hap += i // t
            
        if hap > n:
            _max = i
        elif hap < n:
            _min = i+1
        else:
            m = []
            for t in set(times):
                m.append((i // t) * t)
            return max(m)
        if _max == _min:
            return _min
