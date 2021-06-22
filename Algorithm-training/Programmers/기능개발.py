def get_cost(progresses, speeds):
    costs = []
    for pg, spd in zip(progresses, speeds):
        cost = (100 - pg) // spd
        if (100 - pg) % spd:
            cost+=1
        costs.append(cost)
    return costs

def solution(progresses, speeds):
    answer = []
    costs = get_cost(progresses, speeds)
    max = 0
    for cost in costs:
        if cost > max:
            answer.append(1)
            max = cost
        else:
            answer[-1]+=1
    return answer
