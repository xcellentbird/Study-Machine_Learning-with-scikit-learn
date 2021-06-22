# sort(key = lamda x: f(x)) 잊어버리지 말자
# split을 잘 활용하였다. 잘 숙련된 것 같다.

def solution(s):
    answer = []
    s = [list(map(int,ss.split(','))) for ss in s[2:-2].split('},{')]
    s.sort(key = lambda x: len(x))
    for ss in s:
        for sss in ss:
            if sss not in answer:
                answer.append(sss)
    return answer
