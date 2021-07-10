# STUDY HARD🔥   

## DICTIONARY  
<details>
  <summary><b>AI</b></summary>  
  
  ---
  
  <details>    
    <summary><b>글 모음</b></summary>   
    <p>
    - <a>실리콘밸리의 MLOps Review</a>.  
    
    - <a href="https://github.com/xcellentbird/STUDY/blob/main/AI/%E1%84%89%E1%85%B5%E1%84%80%E1%85%A8%E1%84%8B%E1%85%A7%E1%86%AF%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8.ipynb">시계열 데이터 분석 </a>   
    
    - <a href="https://github.com/xcellentbird/STUDY/blob/main/AI/Tensorflow/tf.GradientTape%EC%9D%98%20%EC%9B%90%EB%A6%AC.md">tf.GradientTape의 원리</a>   
    
    - <a href="https://github.com/xcellentbird/STUDY/blob/main/AI/KDT%20AI/%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%EA%B8%B0%EC%B4%88/Deep_Learning_PyTorch.ipynb">PyTorch 이해하기</a>   
    
    - <a href="https://github.com/xcellentbird/STUDY/blob/main/AI/KDT%20AI/%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%EA%B8%B0%EC%B4%88/Deep_Learning_Tensorflow.ipynb">TensorFlow 이해하기</a>   
    
    - <a href="https://github.com/xcellentbird/STUDY/blob/main/AI/KDT%20AI/%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%EA%B8%B0%EC%B4%88/TensorFlow%20vs%20PyTorch">TensorFlow vs PyTorch</a>   
    </p>
  </details>
  
  <details>    
    <summary><b>용어 모음</b></summary>   
    
    - 표준점수: 훈련 세트의 스테일을 바꾸는 대표적인 방법. 특성의 평균을 빼고 표준편차로 나누는 원리. (잊지 않고 훈련 세트의 평균, 표준편차로 테스트 세트의 표준점수를 내야한다)
    
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
    
    - ensemble _ soft voting: 여러 모델이 레이블 추론 확률들을 각각 레이블 별로 평균을 내어 가장 높은 레이블을 선택하는 기법
    
    - data imbalance(데이터 불균형): 여러 방면으로 데이터가 불균형할 수 있다. 이미지 크기가 다를 수 있고, 각 학습 데이터의 라벨 이미지가 서로 다 다를 수 있다.
    
    - parameter tuning: 모델의 여러 파라미터를 계속 고쳐나가면서 성능을 향상시키는 것.
    
    - data normalization(데이터 정규화): 데이터 feature의 스케일(중요도)을 동일하게(또는 의도적으로 상이하게) 바꾸는 것. 보통 feature값에 평균값을 빼고, 분산값으로 나눈다.
    
    - batch normalization(배치 정규화): 학습률을 너무 높게 잡음으로서 기울기가 소실되거나 발산하는 증상을 예방하는 안정화 방법. 학습 중의 각 계층의 입력값들을 정규화(은닉층의 활성 함수를 정규화)한다. dropout과 같은 일반화 효과를 부수적으로 얻을 수 있다. [참고 영상](https://www.youtube.com/watch?v=nUUqwaxLnWs)
    
    - RMSE(평균 제곱근 오차): 회귀 문제의 성능 지표. 예측값(가설)에 정답값을 빼어 오차를 구하고, 오차를 제곱(절댓값)하여 평균을 낸다. 그 후에 제곱근 값을 취한다.
    
    - receptive field(수용 영역): filter(kernel)가 적용되는 실질적인 필터 크기의 공간을 뜻한다.
    
    - spatial information: 공간 정보. 이미지 상에서 픽셀끼리의 공간적 연결 관계 정보를 뜻한다. 참고로 이미지를 1열로 나열하면 사라지게 된다.
    
    - tranpose-convolution: 크게 padding(?)된 map을 convolution을 통해, 원래의 map보다 더 큰 map을 얻는 것.
    
    - Deconvolution: convolution연산을 거꾸로 수행하는 것. 역산
    
    - backpropagation(역전파): 예측값과 실제값의 오차를 이용하여 가중치를 개선하는 과정
    
    - activation function(활성화 함수)의 종류:
      Sigmoid(0 or 1, Deep하게 사용하면 기울기가 사라지는 단점)
      tanh(-1 or 1, Sigmoid보다는 덜하지만 여전히 Gradient Vanishing 존재)
      ReLU(0 or input, 기울기가 0또는 1이므로 Gradient Vanishing발생 X, exp지수함수가 없어 tanh,sigmoid보다 연산량 6배 빠르다. 하지만 다음 layer가 있을 경우 출력값이 모두 0이 되는 현상이 있다)
      Leaky ReLU(0.1x or x, alpha를 보통 0.1로 설정. ReLU의 한계점 보완), Maxout, ELU(a(e^x-1) or x, exponential linear unit. alpha2도 설정 가능하다. 지수함수가 있어 속도가 빠르지 않은편)
      PReLU(parametric rectified linear unit. ax or x, Leaky LeLU와 비슷하지만 alpha가 학습 가능한 parameter이다)
      SiLU(== Swish, Sigmoid Linear Unit): Sigmoid(x)에 입력값x를 곱한 형태이다. (-)방향으로 갈 수록 0에 수렴하고, 복잡성을 가지고 있어, BatchNormalization과 같이 층을 깊게 쌓을 수 있게 해준다.
    
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
    
    - Active Learning: 지도 학습에서 모든 데이터를 직접 레이블링하지 않고, entropy가 높은 데이터만을 레이블하는 learning 
    
    - Entropy == 불확실성

  </details>
  <details>
    <summary><b>Tips</b></summary>

    - Batch_Size가 학습에 어떤 영향을 미치는지? 배치 사이즈가 커질수록, 조금 더 명확한 최적화 기울기를 얻을 수 있다. 하지만 평평한 경우 안장점(saddle point)에 빠질 위험이 있다. 반대로 배치 사이즈가 작은 경우, 부정확한 기울기를 사용한다는 단점이 있지만, 적은 계산 비용이 들어가므로 한번의 업데이트 동안 여러번 업데이트가 가능하다. 기울기 낮은 공간에서 안장점을 쉽게 빠져나갈 수 있다. 이렇게 장단점이 있지만, 주로 효율성을 위해 배치 사이즈를 메모리 가능한 크게 사용한다. 결과가 크게 다르지 않고, 크게 할 경우, 업데이트 계산 비용을 절약할 수 있기 때문이다.
    
    - Model Ensemble에서 성능이 낮은 모델을 ensemble하는 것만으로도 ensemble 모델의 성능이 좋아진다. 그만큼 parameter 수가 많아지기 때문일 것이라 추측된다.
    
    - BatchNormalization, Dropout, Pooling 적용 순서: Conv - BathcNorm - Activation - Dropout - Pooling [출처](https://gaussian37.github.io/dl-concept-order_of_regularization_term/)
    ↳ 배치 정규화의 목적이 네트워크 연산 결과가 원하는 방향의 분포대로 나오는 것이기 때문에 Conv 연산 뒤에 바로 적용해야 한다.   
  </details>
  <details>
    <summary><b>Engineering</b></summary>

    - CUDA는 GPU를 사용한 연산 가속화 프로그램이다. 성능이 뛰어나지만, NVIDIA의 GPU에서만 이용할 수 있다. 주로 cuDNN API를 사용한다.   
    
    - OpenCL은 CUDA와 비슷하지만, NVIDIA 외의 GPU에서도 사용가능하다는 장점이 있다. 하지만, NVIDIA에서는 연산 속도가 늦다.   
    
    - TensorRT는 다양한 딥러닝 프레임워크에서 학습된 모델을 NVIDIA GPU에 최적화하여 추론 속도를 향상시켜 서비스를 개선하는데 도움을 주는 모델 최적화 엔진이다. - https://developer.nvidia.com/tensorrt 
    
    - GPU 사용에 있어서, 하드 디스크의 데이터를 연산을 위해 GPU에 옮기는 과정에서 병목 현상(GPU로 데이터 전송 속도가 GPU 연산 속도보다 느린 경우)이 일어나 GPU를 효율적으로 사용할 수 없게 된다. 이를 해결하기 위한 해결책으로, 데이터를 모두 RAM에 옮기거나, HDD 대신 SSD를 사용하거나, CPU multi core를 사용하는 방법이 있다.
    
    - Onnx 모듈은 Tensorflow, PyTorch에서 만든 모델들을 export하고, 서로 각 프레임워크 환경 또는 모바일 환경에서 import하여 호환 사용을 가능하게 한다. - https://github.com/onnx/onnx
    
    - FLOPs(FLoating point OPerations): 딥러닝에서 계산량(덧셈, 곱셈 등 연산량)을 뜻한다. 모델의 크기와 효율성을 가늠할 수 있다.
    
    - MAC(Multiply-ACcumulate): FLOPs와 같은 딥러닝에서의 계산량을 뜻한다. 일반적으로 1 MAC = 2 FLOPs가 된다.
  
  
  </details>
  
  ---  
  
</details>

<details>
  <summary><b>Linux</b></summary>
  
  ---  
  
  <details>
    <summary><b>용어</b></summary>
    
    - Shell: 커널(Kernel)과 사용자 간의 다리 역할. 사용자로부터 명령을 받아 해서하고 프로그램을 실행시킴.
    - sh: 최초의 쉘
    - bash: GNU에서 무료로 배포한 업그레이드 쉘. 리눅스의 기본 쉘
    - keystroke: 아무 키나 눌렀을 때 반응 일으키는 것
    
  </details>
  
  <details>
    <summary><b>명령어 모음</b></summary>
    
    - man: 메뉴얼 출력
    - sudo: 관리자 권한 부여
    - apt-get(advanced packaging tool): 패키지 관리 명령어 도구
    - $ sudo apt-get update : 패키지 인덱스 정보 업데이트
    - $ sudo apt-get upgrade : 설치된 패키지 업그레이드
    - $ sudo apt-get install <PACKATE_NAME> : 패키지 설치
    - wget: 웹 링크를 통한 압축 파일 다운로드 도구
    - $ wget <Web Address>
    - rpm: 윈도우에서의 setup.exe와 같은 기능. 실행파일, 설정파일 라이브러리 등이 하나로 묶인 rpm파일을 풀어주는 역할을 한다.
    - chmod: 파일 및 디렉토리의 읽기, 쓰기, 실행 권한 변경. 자세한 설명은 https://blog.naver.com/pk3152/221329487611
    - unmask: 파일이 만들어질 때 권한을 부여
    - mkdir: 디렉토리 생성. 
    ↳ -p: 하위 디렉토리까지 한번에 생성
    - rmdir: 비어있는 디렉토리 삭제
    - .sh 파일: 쉘 스크립트 = 명령어 메크로
    - cd: 디렉토리 이동
    - pwd: 현재 디렉토리 위치
    - ls: 파일 목록 출력
    ↳ -al: 파일 목록 상세 출력
    - cat: 파일 내용 출력
    - rm: 파일 및 폴더 삭제
    ↳ -r: 디렉토리 삭제
    - find or locate: 특정 파일 찾기
    - source: 수정한 스크립트 적용시키기
    - cp <FILENAME>: 파일 복사
    ↳ -r <DIRECTORY>: 디렉토리 복사
    
  </details>
    
  ---
    
</details>

<details>
  <summary><b>React Native</b></summary>
  
  ---  
  
  <details>
    <summary><b>용어 모음</b></summary>
    
    - DOM(Document Object Model) 구조: 클래스와 객체 구조와 유사한 구조. DOM 객체는 부모/자식 형태의 tree 구조를 이룬다.
    
    - rendering(렌더링): 웹 브라우저가 HTML을 parsing하여 js DOM 구조로 만드는 과정.
    
    - 물리 DOM: 렌더링 과정에서 웹 브라우저에서 js 코드가 생성하는 실게 DOM 구조를 뜻한다.
    
    - 가상 DOM: 리액트 코드가 생성한 js 객체 구조.

    - renderer(렌더러): 리액트가 가상 DOM 구조를 물리 DOM 구조로 만드는 기능(rendering)을 수행하는 패키지.

    - Native Renderer: 리액트는 react-dom이라는 DOM 렌더러를 사용하지만, 네이티브는 네이티브 렌더러를 사용한다. 이는 java나 Object-C로 구현된 네이티브 모듈 쪽에서 진행된다.

    - Native Module: 네이티브 모듈 쪽에는 JavaScriptCore 엔진이 동작합니다. 이는 C++언어로 되어있으며, Android에서는 JNI(Java Native interface), iOS에서는 FFI(Foreign. Function interface)방식으로 연결되어 동작합니다.
    
    - JSX(JavaScript XML): XML에 JS을 결합할 용도로 만들어진 구문입니다.
    
    - babel(바벨): JS 컴파일러

  </details>
  
  <details>
    <summary><b>명령어 모음</b></summary>
    
  </details>
    
  ---
    
</details>
  
