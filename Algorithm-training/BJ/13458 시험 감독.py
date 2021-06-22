from sys import stdin

input = stdin.readline

N = int(input())
A = map(int,input().split())
B, C = map(int, input().split())

cnt = 0
for a in A:
    last = a - B
    cnt += 1
    if last <= 0:
        continue

    cnt += last // C
    if last % C:
        cnt += 1

print(cnt)
