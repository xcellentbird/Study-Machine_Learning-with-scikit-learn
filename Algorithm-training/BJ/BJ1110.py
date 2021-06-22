num = int(input())
cnt = 0
n = num
while(True):
    cnt+=1

    a = n % 10
    ten = n // 10
    two = a + ten
    one = two % 10
    answer = a * 10 + one
    n = answer
    
    if n==num:
        break
print(cnt)
