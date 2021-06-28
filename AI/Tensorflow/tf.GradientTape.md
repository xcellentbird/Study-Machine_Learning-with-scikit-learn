## 배경:  
![image](https://user-images.githubusercontent.com/59414764/123679114-1be0d680-d882-11eb-9d5e-8553339ed9d4.png)   



생각해보니 python의 with ... as의 원리가 어떤 건지 생각해본 적이 없었다.
여기에서 with tf.GradientTape() as tape는 어떻게 돌아가는 것일까?   

## Python Docs에서는...   
![image](https://user-images.githubusercontent.com/59414764/123679463-75e19c00-d882-11eb-93a8-6505cc33f99c.png)



=> 간단하게 요약하자면 with를 만났을 때, __enter__()가 호출되고, __enter__()의 반환값이 as 뒤의 변수에 저장된다. 그리고 with 구문을 나가면서 __exit__()함수가 실행되고, 설정된 예외함수가 실행된다는 것이다.


