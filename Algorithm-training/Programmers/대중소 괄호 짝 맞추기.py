def solution(s):
    stack = []
    d = {']':'[', '}':'{',')':'('}
    for ss in s:
        stack.append(ss)
        while len(stack) > 1:
            if stack[-2] == d.get(stack[-1]):
                stack.pop()
                stack.pop()
            else:
                break
    if stack:
        return False
    return True
