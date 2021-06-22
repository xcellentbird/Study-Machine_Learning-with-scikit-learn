def dfs(tickets, track):
    if not tickets:
        return track
    
    #ans = []
    for i, t in enumerate(tickets):
        if t[0] == track[-1]:
            ti = tickets.copy()
            tr = track.copy()
            tr.append(ti.pop(i)[1])
            ans = dfs(ti, tr) #ans += dfs(ti, tr)
            if ans:
                return ans    
    #return ans

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    return dfs(tickets,['ICN'])
