# Decorator: 함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다.
# 주로 전처리나 후처리를 위해 사용하거나 반복을 줄일 때 사용한다.


def deco(func):
    def wrapper(*args, **kwargs):
        print('preprocessing')

        print(func(*args, **kwargs))

        print('post processing')
    return wrapper





@deco
def example():
    print('내부 함수')
    return '반환값'

example()


"""
============= RESTART: C:/Users/path/Decorator_ Python.py =============
preprocessing
내부 함수
반환값
post processing
>>>


"""

print('--------------------------')

# 데코레이터를 epoch처럼 만든다면?

EPOCHS = 10
n = 0
a = 1

def repeat(func):
    print('deco start')
    def wrapper(*args, **kwargs):
        print('inner start')
        if a == 1:
            print('전역변수 사용가능')
        for epoch in range(EPOCHS):
            func(*args, **kwargs)

        print('inner end')
    print('deco end')
    return wrapper


@repeat
def test(cnt):
    global n
    n += cnt
    print(n)


print('테스트 시작')
test(2)


"""
============= RESTART: C:/Users/path/Decorator_ Python.py =============
deco start
deco end
테스트 시작
inner start
전역변수 사용가능
2
4
6
8
10
12
14
16
18
20
inner end
>>>

설명:
먼저 '@'가 쓰인 데코레이터가 먼저 실행이 된다. 하지만 wrapper는 아직 실행되지 않는 상태다
그리고 후에 inner function가 호출될 때, wrapper함수도 호출되고, 내부에 있는 inner function이 실행된다.
