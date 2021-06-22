from heapq import *

def solution(operations):
    min_heap = []
    max_heap = []
    cnt = 0
    for op in operations:
        if not cnt:
            min_heap.clear()
            max_heap.clear()
        
        if op[0] == 'I':
            num = int(op[2:])
            cnt += 1
            heappush(min_heap, num)
            heappush(max_heap, (-num, num))
        elif cnt:
            cnt -= 1
            if len(op) == 3:
                heappop(max_heap)
            else:
                heappop(min_heap)
    if not cnt:
        return [0, 0]
    return [heappop(max_heap)[1], heappop(min_heap)]
