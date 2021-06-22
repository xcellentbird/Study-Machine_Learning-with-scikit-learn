from collections import Counter
def solution(s):
    tmp = []
    if len(s) ==1:
        return 1
    for unit in range(len(s)//2,0,-1):
        comp = ''
        cnt = 1
        cut = [s[c-unit:c] for c in range(unit,len(s)+unit,unit)]
        ret = ''
        for i, part in enumerate(cut):
            if part == comp:
                cnt+=1
            else:
                if cnt > 1:
                    ret += str(cnt) + comp
                else:
                    ret += comp
                comp = part
                cnt = 1
        else:
            if cut[-1]==cut[-2]:
                ret+=str(cnt)
            ret+=cut[-1]
        tmp.append(ret)
    return min(map(len, tmp))
