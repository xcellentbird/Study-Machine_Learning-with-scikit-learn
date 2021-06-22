from pprint import *
from itertools import product
def solution(N, number):
    if N == number:
        return 1
    
    cals = ["+", "-", "//", "*"] # 연산자 모음
    
    # N을 key만큼 사용했을 때 얻을 수 있는 숫자를 value로 하는 dict
    cases = {1:{N}} 
    all_case = {N}
    for t in range(2, 10):
        cases[t] = {int('1'*t) * N} # N, NN, NNN, NNNN ...
        
        # c1 + c2 = t를 만족하는 모든 c1, c2
        for c1 in range(1, t):
            c2 = t - c1 
            
            # N을 c1번 대입해서 나온 숫자와 c2번 대입해서 나온 숫자를 연산
            for n1, n2 in product(cases[c1], cases[c2]):    
                for cal in cals:
                    num = eval(str(n1) + cal + str(n2))
                    if num not in all_case and 0 < num < 32000:
                        cases[t].add(num)
                        all_case.add(num)
                        
        #pprint(cases[t])
        if number in cases[t]:
            return t
    return -1
