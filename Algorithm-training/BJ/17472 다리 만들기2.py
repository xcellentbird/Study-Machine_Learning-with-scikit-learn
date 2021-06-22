from itertools import product
from itertools import combinations
from pprint import pprint
import heapq

MAX_DIST = 100

def bfs(land, now, loc):
    num = land[now[0]][now[1]]
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    stack = [now]
    while stack:
        j, i = stack.pop()
        for dy, dx in dirs:
            if 0 <= dy+j < len(land) and 0 <= dx+i < len(land[0]):
                if land[dy+j][dx+i] == 1:
                    land[dy+j][dx+i] = num
                    stack.append([dy+j, dx+i])
                    loc.append([dy+j, dx+i])
                    
def get_distance(A, B, info_land, land):
    dist = MAX_DIST
    for Aland, Bland in product(info_land[A], info_land[B]):
        if Aland[0] == Bland[0]:
            gap = sorted([Aland[1], Bland[1]])
            for i in range(gap[0]+1, gap[1]):
                if land[Aland[0]][i]:
                    break
            else:
                if dist > gap[1] - gap[0] - 1 and gap[1] - gap[0] not in [1,2]:
                    dist = gap[1] - gap[0] - 1

        elif Aland[1] == Bland[1]:
            gap = sorted([Aland[0], Bland[0]])
            for i in range(gap[0]+1, gap[1]):
                if land[i][Aland[1]]:
                    break
            else:
                if dist > gap[1] - gap[0] - 1 and gap[1] - gap[0] not in [1,2]:
                    dist = gap[1] - gap[0] - 1
    
    if dist == MAX_DIST:
        return 0
    return dist

N, M = map(int, input().split())

# land numbering
land = [list(map(int, input().split())) for _ in range(N)]
num = 2
info_land = {}
for j, i in product(range(N), range(M)):
    if land[j][i] == 1:
        land[j][i] = num
        loc = [[j, i]]
        bfs(land, [j, i], loc)
        loc.sort()
        info_land[num] = loc
        num += 1

#pprint(land)

heap = []
visited = [list(info_land.keys())[0]]
answer = 0
while len(visited) != len(info_land):
    for n in info_land:
        if n not in visited:
            dist = get_distance(visited[-1], n, info_land, land)
            if dist:
                heapq.heappush(heap, (dist, n))
    
    if not heap:
        answer = -1
        break

    while heap:
        score, next_land = heapq.heappop(heap)
        if next_land not in visited:
            visited.append(next_land)
            answer += score
            break

#print(visited)
print(answer)
        

