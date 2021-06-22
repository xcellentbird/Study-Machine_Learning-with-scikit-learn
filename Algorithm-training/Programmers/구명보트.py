from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        answer+=1
        now = people.pop()
        if people and now + people[0] <= limit:
            people.popleft()
    return answer
