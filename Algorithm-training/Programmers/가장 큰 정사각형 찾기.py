def solution(board):
    answer = 0
    width = len(board[0])
    height = len(board)
    
    for side in range(min(width, height), 0, -1):
        for y in range(0, height - side + 1):
            for x in range(0, width - side +1):
                area = 1
                for h in range(y,y+side):
                    if sum(board[h][x:x+side]) != side:
                        break
                else:
                    area = side**2
                    return area
