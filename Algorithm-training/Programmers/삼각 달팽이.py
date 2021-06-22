def solution(n):
    answer = []
    snail = [[0] * a for a in range(1,n+1)]
    cnt = 1
    for nn in range(n):
        mok = nn // 3
        nam = nn % 3
        for nnn in range(n - nn):
            if nam == 0:
                snail[2*mok+nnn][mok] = cnt
                cnt+=1
            if nam == 1:
                snail[-(1+mok)][nnn+1+mok] = cnt
                cnt+=1
            if nam == 2:
                snail[-(2+mok+nnn)][-(1+mok)] = cnt
                cnt+=1
    for i,f in enumerate(snail):
        answer += f
        #print(" "*(len(snail)-1-i), f)
    return answer
