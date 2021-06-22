import pprint
def solution(n, m, image):
    answer = 0
    #padding
    image = list(map(lambda x: [0]+x+[0], image))
    image = [[0 for _ in range(m+2)]] + image + [[0 for _ in range(m+2)]]
    #pprint.pprint(image)
    
    dirs = [[-1,0], [1,0], [0,-1], [0,1]]
    for y in range(1,n+1):
        for x in range(1,m+1):
            color = image[y][x]
            if not color:
                continue
            
            answer+=1
            stack = [[y,x]]
            while stack:
                now_y, now_x = stack.pop()
                now_color = image[now_y][now_x]
                image[now_y][now_x] = 0
                for dy, dx in dirs:
                    neigbor_color = image[now_y+dy][now_x+dx]
                    if neigbor_color and neigbor_color == now_color:
                        stack.append([now_y+dy, now_x+dx])
            #pprint.pprint(image)
    return answer
