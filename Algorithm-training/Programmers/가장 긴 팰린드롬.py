def solution(s):
    # 문자열 길이가 1, 2인 경우
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        if s[0] == s[1]:
            return 2
        return 1
    
    lens = [1 for _ in range(len(s))]
    # 중심으로 할 문자 인덱스 i, ex) 'aba'라면 중심=b, i=1
    for i in range(len(s)): 
        rng = 0 # 범위 길이
        flg = True
        while True:
            # 문자열 길이가 홀수인 경우 ex) 'abcba'
            if s[i-rng:i+1] == s[i:i+rng+1][::-1]:
                lens[i] = 2 * rng + 1
            # 문자열 길이가 짝수인 경우 ex) 'abba'
            elif s[i-rng+1:i+1] == s[i+1:i+rng+1][::-1]: 
                lens[i] = 2 * rng
            else:
                if not flg:
                    break
                # 범위를 2씩 늘려갔기 때문에 -3하여 (-3 + 2 = -1)
                # 이전 범위(-1만큼)를 살펴봅니다
                rng -= 3 
                flg = False
            rng += 2 # 효율성을 위해 범위를 2씩 늘려나갑니다.
    return max(lens)
"""
def solution(s):
    answer = 0
    lengths = []
    
    if len(s) == 1:
        return 1
    
    for i, center in enumerate(s):
        rng = 0
        while s[i-rng:i+1] == s[i:i+rng+1][::-1]:
            rng += 1
            #print(s[i-rng:i+1], s[i:i+rng+1][::-1])
        lengths.append(2 * rng - 1)
    return max(lengths)
"""
