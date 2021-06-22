def solution(dirs):
    move = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    now = [0,0]
    check_loc = []
    for d in dirs:
        dx = move[d][0]
        dy = move[d][1]
        if -5 <= now[0]+dx <= 5 and -5 <= now[1]+dy <= 5:
            new = [now[0] + dx, now[1] + dy]
            if [now, new] not in check_loc:
                check_loc.append([now, new])
                check_loc.append([new, now])
            now = new
    return len(check_loc) / 2
