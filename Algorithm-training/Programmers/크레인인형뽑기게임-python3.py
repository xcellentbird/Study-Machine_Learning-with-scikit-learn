def solution(board, moves):
    answer = 0
    width = len(board[0])
    height = len(board)
    tf = []
    for w in range(width):
        arr = []
        for h in  range(height-1, -1, -1):
            if board[h][w] != 0:
                arr.append(board[h][w])
        tf.append(arr)

    ans = []
    for m in moves:
        if tf[m-1]:
            ans.append(tf[m-1].pop())
            if len(ans) >= 2:
                if ans[-1] == ans[-2]:
                    ans.pop()
                    ans.pop()
                    answer += 2
        
    return answer
