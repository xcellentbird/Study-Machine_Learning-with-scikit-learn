# 최적화에 많이 신경을 쓰려한 티가 많이 보인다.
# 처음에는 O(N^3) 시간 복잡도를 가진 함수였지만, N^2로 최적화하였다.
# 다른 사람 풀이에서는 startwith()함수를 사용하였다.
"""
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
"""

def solution(phone_book):
    answer = True
    phone_book = list(map(list, phone_book))
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return answer
