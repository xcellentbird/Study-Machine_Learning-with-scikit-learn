from collections import Counter
from itertools import combinations

def solution(relation):
    answer = 0
    sets = [[r[i] for r in relation] for i in range(len(relation[0]))]
    check = set()
    
    # combinations를 이용해 index label세트를 만든다
    for N in range(1, len(sets)+1):
        labels = list(combinations(range(len(relation[0])), N))
        
        for label in labels:
            # 이미 체크한 label이라면 continue
            if check & set(label):
                continue

            # 새로운 label을 만든다
            new_label = ['' for _ in range(len(relation))]
            for l in label:
                for i in range(len(relation)):
                    new_label[i] += relation[i][l]
            
            # 새로운 label의 값들이 모두 1이면(==최대값이 1) 답+1, 거쳐간 label 추가
            cnter = Counter(new_label)
            if max(cnter.values()) == 1:
                answer+=1
                check = check | set(label)
    
    return answer
