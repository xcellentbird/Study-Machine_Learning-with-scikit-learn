def min_dict(d, passed):
    min_key = 0
    min_value = float('inf')
    for k, v in zip(d.keys(), d.values()):
        if k not in passed and v < min_value:
            min_value = v
            min_key = k
    return min_key, min_value
    
def solution(N, road, K):
    answer = 0
    for r in road.copy():
        road.append([r[1], r[0], r[2]])
    now = 1
    score = {i: float('inf') for i in range(1, N+1)} # {vill: score}
    score[now] = 0
    passed = []

    while len(passed) != N:
        now = min_dict(score, passed)
        passed.append(now[0])
        for r in road:
            if r[1] not in passed and r[0] == now[0] and r[2] + now[1] < score[r[1]]:
                score[r[1]] = r[2] + now[1]

    for k in score.values():
        if k <= K:
            answer += 1
            
    return answer

"""
def update_route(route):
    for passed in list(reversed(route)):
        if not route[passed]:
            route.popitem()
        else:
            return passed

def get_score(road_map, route):
    score = 0
    towns = list(route.keys())
    start = towns[0]
    for end in towns[1:]:
        score += road_map[start][end]
        start = end
    return score
        
def solution(N, road, K):
    answer = 1
    road_map = {n:{} for n in range(1,N+1)}
    for r in road:
        if r[1] in road_map[r[0]] and road_map[r[0]][r[1]] < r[2]:
            pass
        else:
            if r[2] <= K:
                road_map[r[0]][r[1]] = r[2]
                road_map[r[1]][r[0]] = r[2]
    #print(road_map)
    
    for goal in range(2, N+1):
        now = 1
        route = {now:[]} # route[지나온 마을] = [지나온 마을에서 향할 수 있는 곳]
        found_K = False
        while True:
            if now == goal:
                if get_score(road_map, route) <= K:
                    found_K = True
                    break
                
                route.popitem()
                now = update_route(route)
            else:
                for r in road_map[now]: # route에 없으면 가봐야할 곳 추가
                    if r not in route:
                        if_route = route.copy()
                        if_route[r] = []
                        if get_score(road_map, if_route) <= K: 
                            route[now].append(r)
            
            if not [rv for rv in route if route[rv]]:
                break
                
            if not route[now]:
                now = update_route(route)
            
            if goal in route[now]:
                now = route[now].pop(route[now].index(goal))
            else:
                now = route[now].pop()
            route[now] = []
            
        if found_K:
            answer+=1
            
    return answer
"""
