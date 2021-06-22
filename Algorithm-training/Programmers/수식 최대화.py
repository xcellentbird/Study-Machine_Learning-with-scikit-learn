from itertools import permutations

def solution(expression):
    answer = 0  
    nums = []
    pred = 0
    c = ['-','*','+']
    for i, s in enumerate(expression):
        if s in c:
            nums.append(expression[pred:i])
            nums.append(expression[i])
            pred=i+1
    nums.append(expression[pred:])

    
    for cals in permutations(c, 3):
        n = nums.copy()
        for cal in cals:
            while cal in n:
                i = n.index(cal)
                if i == -1:
                    break
                n.insert(i-1, str(eval(n.pop(i-1) + n.pop(i-1) + n.pop(i-1))))
        nn = abs(int(n[0]))
        if answer < nn:
            answer = nn
    return answer
