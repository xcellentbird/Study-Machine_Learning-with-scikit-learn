def solution(strs, t):
    answer = 0
    
    dict_strs = {}
    for i, s in enumerate(strs):
        if s[0] not in dict_strs:
            dict_strs[s[0]] = []
        dict_strs[s[0]].append(s)
            
    candidates = ['']
    while candidates:
        answer+=1
        tmp = set()
        while candidates:
            now = candidates.pop()
            for s in dict_strs[t[len(now)]]:
                if now + s == t[:len(now+s)]:
                    tmp.add(now+s)
        candidates = list(tmp)
        
        if t in candidates:
            return answer
        
        if len(candidates) > 2:
            candidates = sorted(candidates)[-2:]

    return -1
