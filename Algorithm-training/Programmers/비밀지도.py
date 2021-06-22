def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        ans = ''
        b1 = bin(a1)[2:].zfill(n)
        b2 = bin(a2)[2:].zfill(n)
        for bb1, bb2 in zip(b1, b2):
            if int(bb1) or int(bb2):
                ans+='#'
            else:
                ans+=' '
        answer.append(ans)
    return answer
