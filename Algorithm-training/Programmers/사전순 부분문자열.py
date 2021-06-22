def solution(s):
    stack = [s[0]]
    for i, letter in enumerate(s[1:]):
        while True:
            if stack and stack[-1] < letter:
                stack.pop()
            else:
                stack.append(letter)
                break
    
    return ''.join(stack)
