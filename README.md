# Deep_Learning 

Machine Learning, Deep Learning 공부를 위한 공간입니다.
<details>
  <summary><b>1. KDT AI Dev-Course </b></summary>
  - 자료구조, 알고리즘
  - 인공지능을 위하 수학
</details>
<details>
  <summary><b>2. 책 - 혼공머신 </b></summary>
  
  ![image](https://user-images.githubusercontent.com/59414764/115765205-70c72300-a3e1-11eb-96d1-5a93638f41da.png)
  
  정말 기초 개념 혼자서 공부하기 좋은 책!  
  학교 수업을 복습하기엔 딱이었다.  
   [folder Link](https://github.com/xcellentbird/Deep_Learning/tree/main/%ED%98%BC%EA%B3%B5%EB%A8%B8%EC%8B%A0)  
   [저자 블로그](https://tensorflow.blog/hg-mldl/)
</details>
<details>
  <summary><b>3. Tensorflow/ Keras/ scikit-learn </b></summary>
  
  - API, 함수 모음집
    <details>
    <summary><b>Tensorflow</b></summary>
    </details>
    <details>
    <summary><b>Keras</b></summary>
    </details>
    <details>
    <summary><b>scikit-learn</b></summary>
  
    - sklearn.model_selection.train_test_split(*arrays, test_size, train_size, random_state, shuffle) = return list, length=2*len(arrays)    
    - sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights={‘uniform’, ‘distance’}, algorithm={‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, leaf_size=30(set when algorithm=ball_tree, kd_tree), p=1:manhattan_distance|2:euclidean_distance)    
    - - kn.fit(), kn.get_params(), kn.predict, kn.predict_proba  
    </details>
</details>
<details>
  <summary><b>4. 기계학습 - 강의 복습 노트 </b></summary>
</details>
<details>
  <summary><b>5. 용어사전 </b></summary>
  
  - 표준점수: 훈련 세트의 스테일을 바꾸는 대표적인 방법. 특성의 평균을 빼고 표준편차로 나누는 원리. (잊지 않고 훈련 세트의 평균, 표준편차로 테스트 세트의 표준점수를 내야한다).  
  semi-supervised learning(준지도학습): 지도학습에서 레이블링 작업에 대한 시간과 비용을 줄이고자 나온 방법. 일부만을 레이블링하고(AI에 힌트와 예시를 던져주고), 나머지 데이터는 unsupervised learning(혼자서 깨우치도록)하도록 만든다. [관련 논문 리뷰](https://blog.est.ai/2020/11/ssl/)  
  
  - 온라인 학습에서는 새로운 데이터를 mini-batch 작은 묶음으로 묶어, 시스템을 점진적으로 훈련시킵니다. 반면 오프라인 학습(=out-of-core learning)은 데이터를 모두 한꺼번에 훈련시켜야하므로, 시간과 자원이 많이 필요합니다. Batch Learning이라고도 합니다.
  
  - 머신러닝 시스템에서의 일반화(Generalization)란? 훈련 데이터에서 본 적 없는, 새로운 데이터에서 좋은 예측을 만드는 것 (핸즈온 ML)  
  
</details>
<details>
  <summary><b>6. About AI </b></summary>
  
  [실리콘밸리의 ML옵스 가이드 리뷰](https://github.com/xcellentbird/Deep_Learning/blob/main/%EC%8B%A4%EB%A6%AC%EC%BD%98%EB%B0%B8%EB%A6%AC%EC%9D%98%20ML%EC%98%B5%EC%8A%A4%20%EA%B0%80%EC%9D%B4%EB%93%9C.md)  
  
  ML의 평가
  - 분류 모델 측면 - 정확도(Accuracy) = 예측 결과가 실제와 동일한 데이터 건수 / 전체 예측 데이터 건수.  
  ![image](https://user-images.githubusercontent.com/59414764/115999361-5467f800-a626-11eb-94b3-4fd9cdf463e8.png)

  
</details>
<details>
  <summary><b>+) TMI </b></summary>
  
  - 경량화, 추론 속도 한계가 있을 때는, Tensorrt나 Onnx로 변환시켜 최적화 시킬 수 있다. 하지만 호환되지 않는 몇 함수가 있으므로 확인 후 사용해야한다.
  - Tensorrt: NVDIA GPU를 이용한 모델 최적화 엔진 인터페이스 - https://developer.nvidia.com/tensorrt
  - Onnx: Tensorflow, PyTorch에서 만든 모델들을 export하고, 서로 각 프레임워크 환경 또는 모바일 환경에서 import하여 호환 사용을 가능하게 한다. - https://github.com/onnx/onnx
  
  - PID제어 기법과 딥러닝은 어느 정도 연관성이 있지 않을까? 주로 PID Gain값을 ML을 이용하여 잡아주는 식으로 사용된다.
  
  ![image](https://user-images.githubusercontent.com/59414764/115998955-c4757e80-a624-11eb-8ebc-bfce97b0dc0d.png)  

  ![image](https://user-images.githubusercontent.com/59414764/115998960-cb03f600-a624-11eb-9ac8-6d375ec79584.png)  

  ![PID_Compensation_Animated](https://user-images.githubusercontent.com/59414764/115999012-fd155800-a624-11eb-86b1-1cc614916506.gif)

</details>
