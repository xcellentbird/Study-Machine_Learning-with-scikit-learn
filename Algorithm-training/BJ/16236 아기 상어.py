from sys import stdin
from collections import deque
from itertools import product
#from pprint import pprint
#from copy import deepcopy

# input
N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]
init_size = 2
#print(mp)

# bfs
dirs = [[1,0],[0,-1],[0,1],[-1,0]] # 탐색 순위 결정 .... 을 결정지어주지 않는다

def bfs(start, shark_size):
    #print('start', start, 'shark_size',shark_size)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    queue = deque([start + [0]])
    candidates = []
    
    while queue:
        y, x, t = queue.popleft()
        # candidate가 있으면서, 최근 candidate의 움직인 횟수보다 많이 움직이면 break
        if candidates and candidates[-1][1] < t:
            break
        
        for dy, dx in dirs:
            if 0 <= y+dy < N and 0 <= x+dx < N:
                if not visited[y+dy][x+dx]:
                    
                    there_is = mp[y+dy][x+dx]
                    if there_is > shark_size:
                        continue
                    # 먹잇감을 발견하면 일단 candidates에 넣어놓는다
                    elif there_is and there_is < shark_size:
                        #mp[y+dy][x+dx] = 0
                        #return [[y+dy, x+dx], t+1]
                        candidates.append([[y+dy, x+dx], t+1])
                    
                    visited[y+dy][x+dx] = True
                    queue.append([y+dy, x+dx, t+1])

    # candidate 중 turn이 가장 낮고, 위쪽에 있으며, 왼쪽에 있는 것 return                
    if candidates:
        candi, t = min(candidates, key=lambda x: [x[1]] + x[0])
        mp[candi[0]][candi[1]] = 0
        return [candi, t]
    
    return [start, 0]

def find_babyshark():
    for j, i in product(range(N), range(N)):
        if mp[j][i] == 9:
            mp[j][i] = 0 # 상어 위치 빈자리로
            return [j, i]

#print(bfs(find_babyshark(), init_size))

def play():
    shark_loc = find_babyshark()
    turns = 0
    eat_cnt = 0
    shark_size = init_size
    while True:
        shark_loc, turn = bfs(shark_loc, shark_size)
        """
        print('turns:',turn+turns, 'shakr now:',shark_loc, 'size:',shark_size)
        cp_mp = deepcopy(mp)
        cp_mp[shark_loc[0]][shark_loc[1]] = 9
        pprint(cp_mp)
        """
        
        # 이동하지 않았다면 break
        if not turn:
            return turns
        
        turns += turn
        eat_cnt += 1

        # Level-Up!
        if eat_cnt == shark_size:
            #print('---- Lv Up ----')
            shark_size += 1 # 상어 크기 레베루업!
            eat_cnt = 0 # 먹은 먹이 초기화

print(play())
