from collections import Counter


def solution(healths, items):
    # 체력이 낮은 케릭부터 얼른 무기를 챙겨줘야한다. 
    # 체력 1000짜리 케릭이 낮추는 체력 1짜리 아이템을 사용하기엔 비효율적이기 때문.
    healths.sort()
    mx = healths[-1]
    
    # Linkedlist를 이용함으로써 del시켰을 때 시간복잡도 절약
    healths = Counter(healths) 
    
    # item에 index를 달고, 어차피 최대 체력(health)보다 높은 건 사용 못하니 미리 거른다!
    items = [[item[0], item[1], i+1] for i, item in enumerate(items) if item[1] < mx]
    
    # 목적은 공격치 최대화기 때문에, 공격치 제일 큰 게 앞으로 오게끔 하여 큰 우선순위로 둔다.
    items.sort(reverse=True)

    item_picked = []
    
    # 공격치 높은 것을 최우선으로 비교한다. 
    for up, down, idx in items:
        for health in healths:
            
            # 아이템을 사용한 케릭터는 체력이 100이상 남아야하기 때문에
            if health - down >= 100:
                item_picked.append(idx) # item 찜!
                
                # health가 2개인 것도 있어서 넣은 구문.
                healths[health] -= 1
                
                # healths가 없으면 del! - Linkiedlist를 쓴 이유가 여기에 있다. 시간복잡도 절약
                if not healths[health]:
                    del healths[health]
                    
                break
                
    # 아이템 번호 오름차순 반환
    return sorted(item_picked)
