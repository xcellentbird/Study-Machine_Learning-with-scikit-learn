def flip(board):
    ret = [[0 for _ in range(len(board))] for _ in range(len(board))]
    for j in range(len(board)):
        for i in range(len(board)):
            ret[i][j] = board[j][i]
    return ret

def solution(board, nums):
    answer = 0
    nums = set(nums)
    for line in board:
        if len(set(line) & nums) == len(board):
            answer+=1
            
    board = flip(board)
    
    cross1 = set()
    cross2 = set()
    
    for i, line in enumerate(board):
        cross1.add(line[i])
        cross2.add(line[len(board)-1-i])
        if len(set(line) & nums) == len(board):
            answer+=1
    
    if len(cross1 & nums) == len(board):
        answer+=1
    if len(cross2 & nums) == len(board):
        answer+=1
    
    return answer
