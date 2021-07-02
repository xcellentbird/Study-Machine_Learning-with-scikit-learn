기본적으로 python은 c언어로 만들어진 cpyhon으로 구현되어 있다.  

list는 Array와 같은 형태로 되어 있어, list의 길이나 요소를 바꿀 수 있다. 가변적인 데이터 공간을 사용하도록 선언되기 때문이다.  
하지만, tuple은 struct 구조체로 되어 있어 길이나 요소를 바꿀 수 없다. 딱 필요한 만큼만의 데이터 공간을 사용하도록 선언되기 때문이다.

```
struct {
    int a;
    char b;
    float c;
} foo;

struct foo x = { 3, 'g', 5.9 };
```

그렇다면 이와 같이 구현해 놓은 이유는 무엇일까? 아주 간단하게 말하자면, 최적화를 위해서다. tuple을 사용하면 공간적, 시간적으로 computing 능력을 최적화를 할 수 있다.  
일단 tuple은 필요한 데이터 공간만을 미리 선언하기 때문에, 공간적으로 효율적이라고 볼 수 있다. 또한 list를 사용할 때보다 훨씬 동작 시간이 짧다고 한다.

```
$ python -mtimeit '["fee", "fie", "fo", "fum"]'
1000000 loops, best of 3: 0.432 usec per loop 
$ python -mtimeit '("fee", "fie", "fo", "fum")'
10000000 loops, best of 3: 0.0563 usec per loop
```
 
이렇게 기술적 관점에서 보았을 때, 보관기간이 길고, 불변하는 데이터는 tuple로 저장하는 것이 훨씬 효율적으로 보인다.   
반대로 데이터가 언제든 변할 수 있고, 구조 길이에 의미가 있다면 list를 사용하는 것이 좋다.   

또한 list는 comprehension이 bytecode로 구현되어 있지만, tuple은 comprehension이 구현되어 있지 않다.
```
Python 3.9.2 | packaged by conda-forge | (default, Feb 21 2021, 05:00:30) 
[Clang 11.0.1 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def list():
...     return [a for a in range(3)]
... 
>>> def tuple():
...     return tuple(a for a in range(3))
... 
>>> from dis import dis
```
```
>>> dis(list)
  2           0 LOAD_CONST               1 (<code object <listcomp> at 0x10499e5b0, file "<stdin>", line 2>)
              2 LOAD_CONST               2 ('list.<locals>.<listcomp>')
              4 MAKE_FUNCTION            0
              6 LOAD_GLOBAL              0 (range)
              8 LOAD_CONST               3 (3)
             10 CALL_FUNCTION            1
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x10499e5b0, file "<stdin>", line 2>:
  2           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (a)
              8 LOAD_FAST                1 (a)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE
```
```
>>> dis(tuple)
  2           0 LOAD_GLOBAL              0 (tuple)
              2 LOAD_CONST               1 (<code object <genexpr> at 0x104bbb870, file "<stdin>", line 2>)
              4 LOAD_CONST               2 ('tuple.<locals>.<genexpr>')
              6 MAKE_FUNCTION            0
              8 LOAD_GLOBAL              1 (range)
             10 LOAD_CONST               3 (3)
             12 CALL_FUNCTION            1
             14 GET_ITER
             16 CALL_FUNCTION            1
             18 CALL_FUNCTION            1
             20 RETURN_VALUE

Disassembly of <code object <genexpr> at 0x104bbb870, file "<stdin>", line 2>:
  2           0 LOAD_FAST                0 (.0)
        >>    2 FOR_ITER                10 (to 14)
              4 STORE_FAST               1 (a)
              6 LOAD_FAST                1 (a)
              8 YIELD_VALUE
             10 POP_TOP
             12 JUMP_ABSOLUTE            2
        >>   14 LOAD_CONST               0 (None)
             16 RETURN_VALUE
>>> 

```


+) Namedtuple을 사용하면 dict과 같은 구조체 형태로 만들 수 있다. 이 역시 dict과의 차이점은 데이터와 그 길이가 불변하다는 것이다.   
+) 또한 tuple은 dict의 key값으로도 사용가능하다.   
+) 함수형 프로그래밍에서 args에 tuple형을 넣어 함수를 동작시키는 것도 가능하다. 변수가 다른 요소들에 영향을 받지 않아 훨씬 더 안정적이다.   

-참조-   
[Why is there no tuple comprehension in Python?](https://stackoverflow.com/questions/2174124/why-do-we-need-tuples-in-python-or-any-immutable-data-type)   
[Why do we need tuples in Python or any immutable data type?](https://stackoverflow.com/questions/2174124/why-do-we-need-tuples-in-python-or-any-immutable-data-type)   
[Lists vs Tuples](https://nedbatchelder.com/blog/201608/lists_vs_tuples.html)
