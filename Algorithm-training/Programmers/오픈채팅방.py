def solution(record):
    answer = []
    visitors = {}
    for rec in record:
        rec = rec.split()
        if rec[0][0] == 'L':
            answer.append("{}님이 나갔습니다.".format(rec[1]))
        else:
            visitors[rec[1]] = rec[2]
            if rec[0][0] == 'E':
                answer.append("{}님이 들어왔습니다.".format(rec[1]))
    
    for i, ans in enumerate(answer):
        who, act = ans.split()
        answer[i] = visitors[who[:-2]] + who[-2:] + ' ' + act
    return answer
