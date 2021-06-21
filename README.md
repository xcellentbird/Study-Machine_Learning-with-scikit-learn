# Machine_Learning 

Machine Learning, Deep Learning 공부를 위한 공간입니다.

<details>
  <summary><b>1. 책 - 혼공머신 </b></summary>
  
  ![image](https://user-images.githubusercontent.com/59414764/115765205-70c72300-a3e1-11eb-96d1-5a93638f41da.png)
  
  정말 기초 개념 혼자서 공부하기 좋은 책!  
  학교 수업을 복습하기엔 딱이었다.  
   [folder Link](https://github.com/xcellentbird/Deep_Learning/tree/main/%ED%98%BC%EA%B3%B5%EB%A8%B8%EC%8B%A0)  
   [저자 블로그](https://tensorflow.blog/hg-mldl/)
</details>
<details>
  <summary><b>2. PyTorch/ scikit-learn </b></summary>
  
  - API, 함수 모음집
    <details>
      <summary><b>Pytorch</b></summary>
      - require_grad parameter를 True로 설정하면 자동으로 변화도(미분)를 계산(update)한다는 것이다. 반대로 False로 설정하면 update하지 않는다는 것. 주로 test과정에서는 weight가 update할 필요 없으므로 False로 설정. backward()에 의해 계산(미분)이 시작된다.  
      - optimizer.zero_grad()는, 최적화기에 grad기울기가 쌓여 엉뚱한 방향으로 최적화 되는 것을 막아준다. model도 학습을 위해서 써주기도 한다.  
      - nn.Sequential()과 forward(): 두가지 모두 모델을 설계를 위한 프레임이다. forward는 선언했었던 모델의 각 층을 실행 순서대로 정렬해주는 역할을 한다. Sequential은 초기에 선언과 동시에 정렬하면서 넣어야한다.  
    </details>
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
  <summary><b>3. 기계학습 - 강의 복습 노트 </b></summary>
</details>
<details>
  <summary><b>4. 용어사전 </b></summary>
  
  - 표준점수: 훈련 세트의 스테일을 바꾸는 대표적인 방법. 특성의 평균을 빼고 표준편차로 나누는 원리. (잊지 않고 훈련 세트의 평균, 표준편차로 테스트 세트의 표준점수를 내야한다). 
  
  - semi-supervised learning(준지도학습): 지도학습에서 레이블링 작업에 대한 시간과 비용을 줄이고자 나온 방법. 일부만을 레이블링하고(AI에 힌트와 예시를 던져주고), 나머지 데이터는 unsupervised learning(혼자서 깨우치도록)하도록 만든다. [관련 논문 리뷰](https://blog.est.ai/2020/11/ssl/)  
  
  - 온라인 학습에서는 새로운 데이터를 mini-batch 작은 묶음으로 묶어, 시스템을 점진적으로 훈련시킵니다. 반면 오프라인 학습(=out-of-core learning)은 데이터를 모두 한꺼번에 훈련시켜야하므로, 시간과 자원이 많이 필요합니다. Batch Learning이라고도 합니다.
  
  - 머신러닝 시스템에서의 일반화(Generalization)란? 훈련 데이터에서 본 적 없는, 새로운 데이터에서 좋은 예측을 만드는 것 (핸즈온 ML)  

  - 사례 기반 학습(instance-based learning): 시스템이 훈련 샘플을 기억함으로써 학습하는 방법. 유사도 측정을 사용해 새로운 데이터와 학습한 데이터를 비교하는 방식으로 일반화한다.  

  - 샘플링 잡음(sampling noise): 데이터 샘플이 작아, 데이터가 대표성을 띄지 못 하는 것.
  - 샘플링 편향(sampling bias): 편향된 데이터 샘플이 너무 커서 데이터가 대표성을 띄지 못하는 것

  - 특성 공학(feature engineering): 훈련에 가장 유용한 특성을 선택하고(feature selection), 특성을 결합하여 더 유용한 특성을 만들어(feature extraction), 훈련에 좋은 특성을 만들어내는 것

  - 규제(regularzation): 모델을 단순하게 하고 과대적합의 위험을 감소시키기 위해, 모델에 제약을 가하는 것. 자유도를 줄이는 것. ex) 선형 모델(Wx + b)에서 b를 고정시키거나, 범위를 정한다.

  - 교차 검증(cross-validation): 학습할 데이터에서 여러 개의 검증 데이터셋으로 나누고, 검증 세트마다 나머지 데이터에서 훈련한 모델을 해당 검증 세트에서 평가하도록 하는 것. 단점으로, 검증 세트가 많아 훈련 시간이 길다.  
  
  - Data Augumentation: 기존의 데이터를 이용하여 새로운 데이터를 만드는 것. 이미지를 예로 들자면, 이미지를 뒤집거나, 명암을 바꿀 수 있다. 이를 통해 사물의 좌우 바뀐 모습도 인식할 수 있게 되고, 명암에도 robust하게 된다.
  - model ensemble(모델 앙상블): 서로 다른 모델들을 함께 사용하여 기존보다 성능을 더 올리는 방법 Bagging과 Boosting이 있다.
  - ensemble _ bagging:
  - ensemble _ boosting:
  - ensemble _ hard voting: 여러 모델을 사용하여, 가장 많은 모델이 추론한 label을 선택하는 앙상블 기법
  - ensemble _ soft voting: 여러 모델이 레이블 추론 확률들을 각각 레이블 별로 평균을 내어 가장 높은 레이블을 선택하는 
  - data imbalance(데이터 불균형): 여러 방면으로 데이터가 불균형할 수 있다. 이미지 크기가 다를 수 있고, 각 학습 데이터의 라벨 이미지가 서로 다 다를 수 있다.
  - parameter tuning: 모델의 여러 파라미터를 계속 고쳐나가면서 성능을 향상시키는 것.
  - data normalization(데이터 정규화): 데이터 feature의 스케일(중요도)을 동일하게(또는 의도적으로 상이하게) 바꾸는 것. 보통 feature값에 평균값을 빼고, 분산값으로 나눈다.
  - batch normalization(배치 정규화): 학습률을 너무 높게 잡음으로서 기울기가 소실되거나 발산하는 증상을 예방하는 안정화 방법. 학습 중의 각 계층의 입력값들을 정규화(은닉층의 활성 함수를 정규화)한다. dropout과 같은 일반화 효과를 부수적으로 얻을 수 있다. [참고 영상](https://www.youtube.com/watch?v=nUUqwaxLnWs)
  - RMSE(평균 제곱근 오차): 회귀 문제의 성능 지표. 예측값(가설)에 정답값을 빼어 오차를 구하고, 오차를 제곱(절댓값)하여 평균을 낸다. 그 후에 제곱근 값을 취한다.
  - receptive field(수용 영역): filter(kernel)가 적용되는 실질적인 필터 크기의 공간을 뜻한다.
  - spatial information: 공간 정보. 이미지 상에서 픽셀끼리의 공간적 연결 관계 정보를 뜻한다. 참고로 이미지를 1열로 나열하면 사라지게 된다.
  - tranpose-convolution: 크게 padding(?)된 map을 convolution을 통해, 원래의 map보다 더 큰 map을 얻는 것.
  - Deconvolution: convolution연산을 거꾸로 수행하는 것. 역산
  - FLOPs(FLoating point OPerations): 딥러닝에서 계산량(덧셈, 곱셈 등 연산량)을 뜻한다. 모델의 크기와 효율성을 가늠할 수 있다.
  - MAC(Multiply-ACcumulate): FLOPs와 같은 딥러닝에서의 계산량을 뜻한다. 일반적으로 1 MAC = 2 FLOPs가 된다.
  - backpropagation(역전파): 예측값과 실제값의 오차를 이용하여 가중치를 개선하는 과정
  - activation function(활성화 함수)의 종류: Sigmoid(0 or 1, Deep하게 사용하면 기울기가 사라지는 단점), tanh(-1 or 1, Sigmoid보다는 덜하지만 여전히 Gradient Vanishing 존재), ReLU(0 or input, 기울기가 0또는 1이므로 Gradient Vanishing발생 X, exp지수함수가 없어 tanh,sigmoid보다 연산량 6배 빠르다. 하지만 다음 layer가 있을 경우 출력값이 모두 0이 되는 현상이 있다), Leaky ReLU(0.1x or x, alpha를 보통 0.1로 설정. ReLU의 한계점 보완), Maxout, ELU(a(e^x-1) or x, exponential linear unit. alpha2도 설정 가능하다. 지수함수가 있어 속도가 빠르지 않은편), PReLU(parametric rectified linear unit. ax or x, Leaky LeLU와 비슷하지만 alpha가 학습 가능한 parameter이다)
  - end to end learning(종단간 학습): 입력부터 출력까지 파이프라인 네트워크 없이 한번에 학습하는 방법
  - Transfer Learning과 Fine Tuning: 보통 전이학습이라함은 CNN layer와 이전에 학습된 가중치(weight)를 그대로 가져와, Classifer(분류기, fc)만을 학습시키는 것(Fine Tuning)을 뜻한다.
  - K-Fold Cross Validation: training dataset을 K개로 나누고, 한 파트씩 번갈아가며 validation dataset으로 지정한다. validation dataset에 대한 error을 반영할 수 있고, 전체 데이터셋을 학습시킬 수 있다는 장점이 있다. 하지만, 그만큼 학습 시간이 늘어난다.
  - outlier: 잘못 평가된 값으로, 결과적으로 잘못된 분석 겨로가를 초래할 수 있는 값들을 의미한다. [참고](https://ourcstory.tistory.com/142) 독립된 모델 앙상블 기법을 통해 해결할 수 있을 것으로 보인다.
  - attention feature: 데이터에서 원하고자 하는 feature에 가중치를 두는 것. ex) Image 데이터에서 image의 가로 세로 크기를 추가 feature로 삼는다
  - depth wise separable convolution: 채널을 한번에 3차원 kernel로 컨볼루션을 시행하지 않고, 채널을 나누어 2차원 kernel로 각각 컨볼루션 후 다시 곂쳐놓는다. 그리고 [1, 1, depth]크기의 컨볼루션을 한번 더 수행하여 한 개의 채널 결과값(2차원)을 얻어낸다. 이러한 과정을 수행하는 이유는 연산량을 줄이기 위해서다.
  - pointwise convolution: 1x1xChannel_size 크기의 filter를 이용하여 컨볼루션을 수행한다. 즉, 다채널 영상을 더 적은 채널의 영상으로 embedding하는 것으로 해석할 수 있다. 채널 수를 줄임으로서 연산량을 줄여 속도를 높일 수 있지만, 중요 정보가 손실 될 수 있다는 단점을 가지고 있다. = Channel Reduction이라고도 한다.
  - grouped convolution: 여러 개의 채널을 한꺼번에 컨볼루션 수행하지 않고, 채널을 그룹으로 나누어 따로 컨볼루션을 수행 후 다시 합치는 방법이다. 기존의 CNN과 낮은 연산량을 요구하고, 각 그룹에서 채널끼리 상호 관계가 맺어져 학습이 될 수 있다는 특징이 있다. 그리고 병렬 처리에 유리하다는 장점 또한 가지고 있다.
  - deformable convolution: 단순하게 filter의 weight를 학습하는 것이 아니라 kernel의 모양(kernel offset: sampling grid의 스케일 종횡비, 회전 방식 등)도 함께 학습하는 것이다. 즉 object의 크기에 대해서 유연하게 학습이 가능하다.
  - 1x1 convolution: Channel 수를 조절할 수 있게 되고, 이를 이용하여 계산량을 줄일 수 있다. 또한 그에 따라 모델을 깊게 쌓을 수 있게 되므로, 더 많은 ReLU Activation을 사용할 수 있게 되어 비선형성을 늘릴 수도 있다.Xception, Googlenet, Moblienet 등 1x1 conv 방법을 채택하였다.
  - SiLU(== Swish, Sigmoid Linear Unit): Sigmoid(x)에 입력값x를 곱한 형태이다. (-)방향으로 갈 수록 0에 수렴하고, 복잡성을 가지고 있어, BatchNormalization과 같이 층을 깊게 쌓을 수 있게 해준다.
</details>
<details>
  <summary><b>7. About AI </b></summary>
  
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

  - Batch_Size가 학습에 어떤 영향을 미치는지? 배치 사이즈가 커질수록, 조금 더 명확한 최적화 기울기를 얻을 수 있다. 하지만 평평한 경우 안장점(saddle point)에 빠질 위험이 있다. 반대로 배치 사이즈가 작은 경우, 부정확한 기울기를 사용한다는 단점이 있지만, 적은 계산 비용이 들어가므로 한번의 업데이트 동안 여러번 업데이트가 가능하다. 기울기 낮은 공간에서 안장점을 쉽게 빠져나갈 수 있다. 이렇게 장단점이 있지만, 주로 효율성을 위해 배치 사이즈를 메모리 가능한 크게 사용한다. 결과가 크게 다르지 않고, 크게 할 경우, 업데이트 계산 비용을 절약할 수 있기 때문이다.
</details>
