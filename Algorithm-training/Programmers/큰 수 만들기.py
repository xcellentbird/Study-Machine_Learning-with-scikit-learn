def solution(number, k):
    answer = 0
    i = 0
    cnt = 0
    while cnt < k:
        if i < len(number)-1:
            if number[i] >= number[i+1]:
                i = i+1
            else:
                number = number[:i] + number[i+1:]
                cnt +=1
                i-=1
        else:
            number = number[:-1]
            cnt+=1
            i-=1
        
        if i<0:
            i=0
    return number
