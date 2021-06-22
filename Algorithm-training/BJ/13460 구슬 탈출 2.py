from sys import stdin
from collections import deque
from itertools import product

input = stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = []
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 방향만을 설정해주는 dirs

ri, rj, bi, bj = 0, 0, 0, 0
for i, j in product(range(N), range(M)):
    if board[i][j] == 'R':
        ri, rj = i, j
    if board[i][j] == 'B':
        bi, bj = i, j

def move(i, j, di, dj):
    cnt = 0
    # 움직일 위치가 벽이 아니고, 현재 위치가 구멍이 아닐 때까지
    while board[i+di][j+dj] != '#' and board[i][j] != 'O':
        i, j = i+di, j+dj
        cnt += 1

    # 벽에 부딪쳣거나 위치가 구멍인 경우 반환
    return i, j, cnt

def play(ri, rj, bi, bj, d):
    que = deque([(ri, rj, bi, bj, d)])
    visited.append((ri, rj, bi, bj))

    while que:
        sri, srj, sbi, sbj, sd = que.popleft()
        #print(sd, '-','red:',sri, srj, ' blue:',sbi, sbj)
        if sd > 10:
            return -1

        for di, dj in dirs:
            nri, nrj, rcnt = move(sri, srj, di, dj)
            nbi, nbj, bcnt = move(sbi, sbj, di, dj)

            # 파랑 구슬이 구멍에 도착한 경우(node)는 무시!, que에 넣지 않는다.
            if board[nbi][nbj] != 'O':
                # 빨간 구슬이 구멍에 도착했을 때 ret
                if board[nri][nrj] == 'O':
                    return sd

                # 파랑 구슬, 빨간 구슬이 같은 위치에 있을 때
                if nri == nbi and nrj == nbj:
                    # 빨간 구슬이 더 많이 움직였으면, 한 칸 뒤로
                    if rcnt > bcnt:
                        nri, nrj = nri-di, nrj-dj
                    # 파랑 구슬이 더 많이 움직였으면, 한 칸 뒤로
                    else:
                        nbi, nbj = nbi-di, nbj-dj

                if (nri, nrj, nbi, nbj) not in visited: 
                    visited.append((nri, nrj, nbi, nbj))
                    que.append((nri, nrj, nbi, nbj, sd+1))
    return -1

turn = play(ri, rj, bi, bj, 1)
print(turn)
