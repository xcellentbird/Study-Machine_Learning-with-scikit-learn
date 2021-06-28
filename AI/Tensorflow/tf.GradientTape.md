배경:  
![image](https://user-images.githubusercontent.com/59414764/123679114-1be0d680-d882-11eb-9d5e-8553339ed9d4.png)   


Tensorflow 2.0의 Eager모드에서는 다음과 같이 구성되어 다이나믹 연산이 이루어진다.   
배우면서 생각해보니 python의 with ... as의 원리가 어떤 건지 생각해본 적이 없었다.
여기에서 with tf.GradientTape() as tape는 어떻게 돌아가는 것일까?    

   
[Python Docs](https://docs.python.org/ko/3/reference/compound_stmts.html#try)에서는...   
![image](https://user-images.githubusercontent.com/59414764/123679463-75e19c00-d882-11eb-93a8-6505cc33f99c.png)


=> 간단하게 요약하자면 with를 만났을 때, __enter__()가 호출되고, __enter__()의 반환값이 as 뒤의 변수에 저장된다. 그리고 with 구문을 나가면서 __exit__()함수가 실행되고, 설정된 예외함수가 실행된다는 것이다.


이번에는 tensorflow의 Github를 뒤져보자 [tf.GradientTape](https://github.com/tensorflow/tensorflow/blob/v2.5.0/tensorflow/python/eager/backprop.py#L731-L1342)   
![image](https://user-images.githubusercontent.com/59414764/123680279-7890c100-d883-11eb-9b47-4cb3beab757f.png)   
역시나 enter와 exit함수가 있었다. with함수를 만났을 때 GradientTape의 인스턴스가 as 뒤의 Tape 변수에 담겨 객체로 생성되는 것처럼 보인다.   
그리고 그 전에 push_tape 함수가 호출되는 것을 볼 수 있다.   
![image](https://user-images.githubusercontent.com/59414764/123682324-d3c3b300-d885-11eb-9c50-fff4964cc068.png)

간단하게 해석하자면, tape(auto grad graph)가 이미 기록되고(돌아가고)있으면 오류를 발생시키고, 중단된 tape가 있으면 이어서 실행, 그리고 없다면 tape.push_new_tape()를 호출하여 새로운 tape를 stack에 push한다. 그리고 push된 tape를 객체의 _ tape 변수에 저장되는 원리다. 그리고 기록 중이라는 flag를 True로 띄운다   

with구문을 나가게 되면 exit()가 호출된다. exit함수는 아주 간단하다. tape가 기록 중에 있으면 pop_tape()를 호출한다.   
그리고 pop_tape는...   
![image](https://user-images.githubusercontent.com/59414764/123685326-847f8180-d889-11eb-8d9b-1c1af53d72b6.png)   
tape가 기록 중이지 않을 때 오류를 발생시키고, 기록 중이었다면, 기록한 tape_를 tape의 pop_tape함수에 담아 실행시키면 stack에 있는 tape가 pop된다(pop된 tape는 GradientTape 인스턴스의 _ tape에 저장된 상태인 것으로 추측이 된다). 그리고나서 기록 flag를 False로 바꿔주면서 기록을 끝낸다.


마지막으로 tf.GradientTape.gradient(self, target, sources, output_gradients, unconnected_gradients) 함수로 grad를 반환받는다.   
![image](https://user-images.githubusercontent.com/59414764/123686519-da085e00-d88a-11eb-8ecc-e68a021399ac.png)   
target: 미분을 실행할 Tensor or Variable 가 담긴 구조체를 넣는다.   
sources: target의 미분 대상인 Tensor or Variable들을 넣는다.   
output_gradients: 넣은 target의 각 요소들의 미분값들을 해당 입력 변수에 담는다(반환 값이 달라지진 않는다).   
[unconnected_gradients](https://github.com/tensorflow/tensorflow/blob/a4dfb8d1a71385bd6d122e4f27f86dcebb96712d/tensorflow/python/ops/unconnected_gradients.py#L27): sources에 대한 target의 미분 값이 0일 경우(target의 변수에 sources가 없거나, relu같은 활성화함수에 의해 0을 미분할 경우) 반환값을 어떤 값으로 대체할 지 정하도록 한다. NONE, ZERO를 넣을 수 있다. (계산과정에서 어떠한 차이가 있을 지는 모르겠다...)   
요약하자면, 함수의 입력 변수들과 기록된 tape 정보들을 고려하여 imperative_grad 함수를 통해 기울기를 계산해낸다. 그리고 계산된 가중치의 기울기(grad)를 반환한다. 다시말해, gradient함수를 호출될 때 기울기가 계산되어 반환된다.

