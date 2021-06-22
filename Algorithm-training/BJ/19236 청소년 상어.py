from sys import stdin
from collections import deque
from itertools import product
from pprint import pprint
from copy import deepcopy

#input
mp_size = 4
shark = -1
dirs = {1:[-1, 0], 2:[-1, -1], 3:[0, -1], 4:[1, -1], 5:[1,0], 6:[1, 1], 7:[0, 1], 8:[-1, 1]}

input = stdin.readline
inp = [list(map(int, input().split())) for _ in range(mp_size)]

fish_head = {}
fish_map = [[0] * mp_size for _ in range(mp_size)]

for j, i in product(range(mp_size), range(0,mp_size*2,2)):
    fish_num = inp[j][i]
    fish_map[j][i//2] = fish_num
    fish_head[fish_num] = [j, i//2, inp[j][i+1]]

shark_head = [0, 0, 0]
#pprint(fish_map)
#print(fish_head)

def fish_move(fh, fm, sh):
    for fish in sorted(fh.keys()):
        y, x, head = fh[fish]

        while True:
            ny, nx = y + dirs[head][0], x + dirs[head][1]
            if 0 <= ny < mp_size and 0 <= nx < mp_size and (ny != sh[0] or nx != sh[1]):
                fh[fish][2] = head
                # 물고기 위치 change
                if not fm[ny][nx]:
                    fh[fish][0] = ny
                    fh[fish][1] = nx
                else:
                    fh[fm[ny][nx]][0], fh[fish][0] = fh[fish][0], fh[fm[ny][nx]][0]
                    fh[fm[ny][nx]][1], fh[fish][1] = fh[fish][1], fh[fm[ny][nx]][1]
                fm[ny][nx], fm[y][x] = fm[y][x], fm[ny][nx] # 맵 갱신
                break
            
            if head == 8:
                head = 1
            else:
                head+=1
            
def can_go(fm, sh):
    ret = []
    y, x, head = sh
    while True:
        y, x = y + dirs[head][0], x + dirs[head][1]
        if y < 0 or x < 0 or y >= mp_size or x >= mp_size:
            break
        
        if fm[y][x] not in [-1, 0]:
            ret.append(fm[y][x])
    return ret

def eat_fish(fish, fh, fm, sh):
    fm[sh[0]][sh[1]] = 0
    sh = fh.pop(fish)
    fm[sh[0]][sh[1]] = -1
    return fh, fm, sh
    
answers = []
def dfs(score, fh, fm, sh):
    fish_move(fh, fm, sh)
    
    next_fishes = can_go(fm, sh)
    if not next_fishes:
        answers.append(score)
        
    for next_fish in next_fishes:
        cp_fh = deepcopy(fh)
        cp_fm = deepcopy(fm)
        cp_sh = deepcopy(sh)

        cp_fh, cp_fm, cp_sh = eat_fish(next_fish, cp_fh, cp_fm, cp_sh)
        dfs(score + next_fish, cp_fh, cp_fm, cp_sh)


def shark_init():
    ret = fish_map[0][0]
    shark_head[2] = fish_head.pop(fish_map[0][0])[2]
    fish_map[0][0] = -1
    return ret

dfs(shark_init(), fish_head, fish_map, shark_head)
print(max(answers))

    
