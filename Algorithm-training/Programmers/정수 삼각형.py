def solution(triangle):
    answer = 0
    for row in range(1, len(triangle)):
        for i in range(len(triangle[row])):
            start = i-1
            if start < 0:
                start = 0
            triangle[row][i] += max(triangle[row-1][start:i+1])
    return max(triangle[-1])
