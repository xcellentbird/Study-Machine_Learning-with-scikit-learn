def solution(arr):
    times = 1
    arr.sort()
    while True:
        num = arr[-1] * times
        for n in arr[:-1]:
            if num % n:
                break
        else:
            return num
        times+=1
