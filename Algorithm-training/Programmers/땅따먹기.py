def solution(land):
    for row in range(1, len(land)):
        for i, n in enumerate(land[row]):
            land[row][i] += max(land[row-1][:i] + land[row-1][i+1:])
    return max(land[-1])
