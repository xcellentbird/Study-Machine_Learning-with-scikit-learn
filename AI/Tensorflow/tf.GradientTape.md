배경:  
![image](https://user-images.githubusercontent.com/59414764/123679114-1be0d680-d882-11eb-9d5e-8553339ed9d4.png)   


Tensorflow 2.0의 Eager모드에서는 다음과 같이 구성되어 다이나믹 연산이 이루어진다.   
배우면서 생각해보니 python의 with ... as의 원리가 어떤 건지 생각해본 적이 없었다.
여기에서 with tf.GradientTape() as tape는 어떻게 돌아가는 것일까?    

   
Python Docs에서는...   
![image](https://user-images.githubusercontent.com/59414764/123679463-75e19c00-d882-11eb-93a8-6505cc33f99c.png)


=> 간단하게 요약하자면 with를 만났을 때, __enter__()가 호출되고, __enter__()의 반환값이 as 뒤의 변수에 저장된다. 그리고 with 구문을 나가면서 __exit__()함수가 실행되고, 설정된 예외함수가 실행된다는 것이다.


이번에는 tensorflow의 Github를 뒤져보자 [tf.GradientTape](https://github.com/tensorflow/tensorflow/blob/v2.5.0/tensorflow/python/eager/backprop.py#L731-L1342)   
![image](https://user-images.githubusercontent.com/59414764/123680279-7890c100-d883-11eb-9b47-4cb3beab757f.png)   
역시나 enter와 exit함수가 있었다. with함수를 만났을 때 GradientTape의 인스턴스가 as 뒤의 Tape 변수에 담겨 객체로 생성되는 것처럼 보인다.   
그리고 그 전에 push_tape 함수가 호출되는 것을 볼 수 있다.   
![image](https://user-images.githubusercontent.com/59414764/123682324-d3c3b300-d885-11eb-9c50-fff4964cc068.png)

간단하게 해석하자면, tape(auto grad graph)가 이미 기록되고(돌아가고)있으면 오류를 발생시키고, 중단된 tape가 있으면 이어서 실행, 그리고 없다면 새로운 tape를 원리다. 그리고 기록 중이라는 flag를 True로 띄운다   

with구문을 나가게 되면 exit()가 호출된다. exit함수는 아주 간단하다. tape가 기록 중에 있으면 pop_tape()를 호출한다.   
그리고 pop_tape는...   
![image](https://user-images.githubusercontent.com/59414764/123682991-ad524780-d886-11eb-9674-1d8749de1d1c.png)
tape가 기록 중이지 않을 때 오류를 발생시키고, 기록 중이었다면, 기록한 tape_를 tape의 pop_tape함수에 담아 실행시키면 stack에 있는 tape가 pop된다(pop된 tape는 GradientTape 인스턴스에 저장될 것으로 추측이 된다). 그리고나서 기록 flag를 False로 바꿔주면서 기록을 끝낸다.
