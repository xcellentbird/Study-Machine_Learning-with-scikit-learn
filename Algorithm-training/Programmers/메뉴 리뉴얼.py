from itertools import combinations

def solution(orders, course):
    answer = []
    for count in course:
        combs = []
        for foods in orders:
            if len(foods) >= count:
                combs += [''.join(sorted(c)) for c in list(combinations(foods, count))]
        
        candidates = list(set(sorted(combs)))
        counts = [combs.count(candidate) for candidate in candidates]
        
        if counts and max(counts) > 1:
            for i, c in enumerate(counts):
                if c == max(counts):
                    answer.append(candidates[i])
                
    return sorted(answer)
