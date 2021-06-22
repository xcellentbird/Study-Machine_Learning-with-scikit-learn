from itertools import product

N = int(input())

gnd = [[0] * N for _ in range(N)]
mp = [list(input()) for _ in range(N)]

for y, x in product(range(N), repeat=2):
    if mp[y][x] == '1' and not gnd[y][x]
