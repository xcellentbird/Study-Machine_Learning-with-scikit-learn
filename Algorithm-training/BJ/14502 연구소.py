from sys import stdin
#from pprint import pprint
from itertools import product
from itertools import combinations

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def padding(rooms):
    return [[1] * (M+2)] +[[1] + r+ [1]for r in rooms] + [[1] * (M+2)]


def get_room_info():
    emty = []
    virus = []
    for j, i in product(range(N+2), range(M+2)):
        if rooms[j][i] == 0:
            emty.append([j, i])
        elif rooms[j][i] == 2:
            virus.append([j, i])
            
    return emty, virus


def bfs(tmp_walls, virus):
    cnt_virus = 0
    visited = [[False] * len(rooms[0]) for _ in rooms]

    # 가벽이 있는 곳은 방문한 곳으로 설정하여, bfs가 찾지 못하도록 설정
    for wy, wx in tmp_walls:
        visited[wy][wx] = True
        
    while virus:
        vy, vx = virus.pop()
        for dy, dx in dirs:
            if not visited[vy+dy][vx+dx] and rooms[vy+dy][vx+dx] not in [1, 2]:
                visited[vy+dy][vx+dx] = True
                cnt_virus += 1
                virus.append([vy+dy, vx+dx])

    return cnt_virus

# 가벽을 세울 수 있는 모두의 경우수를 대입하여 bfs 실행
def play(emty, virus):
    for tmp_walls in combinations(emty, 3):
        emty_cnt = len(emty) - 3
        answers.append(emty_cnt - bfs(tmp_walls, virus.copy()))

# input
input = stdin.readline
N, M = map(int, input().split())
rooms = padding([list(map(int, input().split())) for _ in range(N)])
answers = []

emty, virus = get_room_info()
play(emty, virus)

print(max(answers))
