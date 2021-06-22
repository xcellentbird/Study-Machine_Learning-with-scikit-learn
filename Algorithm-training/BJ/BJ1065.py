C = int(input())
cnt = 99
if C < 100:
    cnt = C
else:
    for i in range(100,C+1):
        s = str(i)
        gap = int(s[0]) - int(s[1])
        for n in range(1, len(s)-1):
            if gap != int(s[n]) - int(s[n+1]):
                break
            if n == len(s)-2:
                cnt+=1
print(cnt)
