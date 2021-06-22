C = int(input())
case = []
for i in range(C):
    arr = list(map(int,input().split()))
    arr = arr[1:]
    avr = sum(arr) / len(arr)
    student = 0
    for t in arr:
        if t > avr:
            student+=1
    case.append(student/len(arr))
        
for i in case:
    print(str(round(i*100, 3)) + '%')
