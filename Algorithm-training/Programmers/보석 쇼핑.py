def solution(gems):
    start = 1
    end = 100000
    gm = {g:[] for g in set(gems)}
    st2ed = 100000
    for i, now in enumerate(gems):
        gm[now].append(i+1)
        
        flg = True
        for g in gm:
            if not gm[g]:
                flg = False
                break
        
        if flg:
            tmp_start = min([gm[g][-1] for g in gm if gm[g]])
            tmp_end = max([gm[g][-1] for g in gm if gm[g]])
            if st2ed > tmp_end - tmp_start:
                start = tmp_start
                end = tmp_end
                st2ed = end - start
                
    return [start, end]
