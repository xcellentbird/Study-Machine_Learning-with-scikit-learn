from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        mn = heappop(scoville)
        if mn >= K:
            break
        if not scoville:
            return -1
        answer+=1
        heappush(scoville, mn + heappop(scoville) * 2)
    return answer
