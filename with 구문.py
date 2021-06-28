# with 구문은 확실한 garbage collect를 위해 사용됩니다. 주로 open(), close() 함수와 같이 쓰입니다.
# https://docs.python.org/ko/3/reference/compound_stmts.html#the-with-statement
# https://docs.python.org/ko/3/reference/datamodel.html#context-managers


class with_test:
    def __init__(self):
        # 생성자
        print('객체 생성')

    def is_alive(self):
        print("i'm not garbage")

    def in_context(self):
        print('--- context ---')
    
    def __enter__(self):
        print('with context 진입')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with context 종료. 예외 함수를 넣지 않았습니다')



print('start')

with with_test() as ret:
    ret.in_context()

print('end')

ret.is_alive()

test = with_test()
print('with을 통해 만들어진 객체와 with 후에 만들어진 객체는 서로 다른 객체다',ret != test)



"""
실행 결과:
================= RESTART: C:/Users/path/with 구문.py =================
start
객체 생성
with context 진입
--- context ---
with context 종료. 예외 함수를 넣지 않았습니다
end
i'm not dead
객체 생성
with을 통해 만들어진 객체와 with 후에 만들어진 객체는 서로 다른 객체다 True
>>> 
