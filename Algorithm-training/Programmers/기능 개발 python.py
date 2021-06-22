"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
"""


def solution(pgs, spds):
    answer = []
    ready = [False for _ in pgs]
    day = 0
    out = []
    while(True):
        day+=1
        before = len(out) # 어제까지의 배포량 
        
        # 작업, 진전도 상승시키기
        for idx in range(len(pgs)):
            pgs[idx] += spds[idx]
            if pgs[idx] >= 100:
                ready[idx] = True
        
        #배포하기
        for idx in range(len(pgs)):
            if idx == 0:
                if ready[idx] and idx not in out:
                    out.append(idx)
            else:
                # 준비, 배포 안 됐고, 이전 기능이 배포됨
                if ready[idx] and (idx not in out) and idx-1 in out:
                    out.append(idx)
        
        # 배포 개수 카운트
        done = len(out) - before
        if done: # 0일 때 제외
            answer.append(done)
            
        # 디버깅
        print("day: ", day)
        print("- pgs: ", pgs)
        print("- ready: ", ready)
        print("- out: ", out)
        
                    
        # 런타임 아웃 방지
        if len(out) == len(pgs): break
        elif day > 100: break
    return answer
