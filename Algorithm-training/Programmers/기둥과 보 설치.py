def possible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:
            if y != 0 and (x, y-1, COL) not in result and (x-1, y, ROW) not in result and (x, y, ROW) not in result:
                return False
        else:
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return False
    return True

def solution(n, build_frame):
    result = set()
    
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:
            result.add(item)
            if not possible(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if not possible(result):
                result.add(item)
    
    return sorted(map(list, result), key = lambda x : (x[0], x[1], x[2]))
