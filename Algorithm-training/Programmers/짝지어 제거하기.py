def solution(s):
    solo = []
    for i in range(len(s)):
        if not solo or s[i] != solo[-1]:
            solo.append(s[i])
        else:
            solo.pop()
    
    if solo:
        return 0
    return 1
