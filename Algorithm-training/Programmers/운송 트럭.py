def solution(max_weight, specs, names):
    answer = 1
    specs = {goods[0]: int(goods[1]) for goods in specs}
    weight = 0
    for name in names:
        if weight + specs[name] > max_weight:
            answer+=1
            weight = specs[name]
        else:
            weight+= specs[name]
    return answer
