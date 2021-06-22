from sys import stdin
from pprint import pprint
from collections import deque
from itertools import product

input = stdin.readline
N, L, R = map(int, input().split())
#print(N, L, R)

popu = [list(map(int, input().split())) for _ in range(N)]
#pprint(popu)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(start):
    union = [start]
    queue = deque([start])
    while queue:
        j, i = queue.popleft()

        for dj, di in dirs:
            if 0 <= j+dj < N and 0 <= i+di < N:
                if L <= abs(popu[j][i] - popu[j+dj][i+di]) <= R:
                    if [j+dj, i+di] not in union:
                        union.append([j+dj, i+di])
                        queue.append([j+dj, i+di])
    return union

def get_unions():
    unions = []
    visited = []
    for j, i in product(range(N), repeat=2):
        if [j, i] not in visited: #sum(unions, []):
            u = bfs([j, i])
            unions.append(u)
            visited += u
    return unions

#print(get_unions())

pred_len = 0
def move():
    global pred_len
    unions = get_unions()

    if len(unions) == pred_len:
        return False
    else:
        pred_len = len(unions)
    
    while unions:
        union = unions.pop()
        sum_popu = sum(map(lambda x: popu[x[0]][x[1]], union))
        #print(sum_popu)

        next_popu = sum_popu // len(union)
        for j, i in union:
            popu[j][i] = next_popu

    return True       

def main():
    day = -1
    while move():
        day += 1

    print(day)

main()
