def solution(monster, S1, S2, S3):
    answer = 0
    for x1 in range(1, S1+1):
        for x2 in range(1, S2+1):
            for x3 in range(1, S3+1):
                if x1+x2+x3+1 not in monster:
                    answer+=1
    return int(answer * 1000 / (S1 * S2 * S3))
