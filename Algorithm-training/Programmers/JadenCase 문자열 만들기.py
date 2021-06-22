def solution(s):
    answer = ''
    flg = True
    for ss in s:
        if flg:
            ss = ss.upper()
            flg = False
        else:
            ss = ss.lower()

        if ss == ' ':
            flg = True
        answer+=ss
    return answer
