# 풀이 5시간짜리...
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0 for _ in range(bridge_length)]) # 아무것도 없는 상태 [0, 0, 0, 0, ...]
    time = 0
    while True:
        time+=1 # 시간 카운트
        on_bridge.popleft()
        go_on = 0
        if truck_weights: # on_bridge에 넘을 게 남아있으면
            if weight - sum(on_bridge) >= truck_weights[0]: # 무게 측정
                go_on = truck_weights.popleft()
            else:
                # bridge가 길고 소수의 트럭만이 있을 때, 빨리 감기 
                for i, w in enumerate(on_bridge):
                    if w:
                        time+=i
                        on_bridge = deque(list(on_bridge)[i:] + list(on_bridge)[:i])
                        break
        else:
            return time + bridge_length - 1
        
        on_bridge.append(go_on)
        
"""
테스트 1 〉통과 (0.28ms, 10.3MB)
테스트 2 〉통과 (13.14ms, 10.3MB)
테스트 3 〉통과 (0.02ms, 10.2MB)
테스트 4 〉통과 (10.02ms, 10.3MB)
테스트 5 〉통과 (70.55ms, 10.3MB)
테스트 6 〉통과 (28.84ms, 10.3MB)
테스트 7 〉통과 (0.23ms, 10.2MB)
테스트 8 〉통과 (0.07ms, 10.1MB)
테스트 9 〉통과 (1.66ms, 10.3MB)
테스트 10 〉통과 (0.07ms, 10.3MB)
테스트 11 〉통과 (0.02ms, 10.2MB)
테스트 12 〉통과 (0.21ms, 10.2MB)
테스트 13 〉통과 (0.51ms, 10.1MB)
테스트 14 〉통과 (0.02ms, 10.2MB)
"""
