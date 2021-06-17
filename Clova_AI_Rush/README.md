2021-5-18 ~ 2021-6-4 18일 동안 치뤘던 AI Rush 2021 해커톤에 대한 리뷰입니다. 데이터와 일부 사항에 대해서는 회사 기밀에 해당하는 사항이라 언급할 수 없음을 미리 알려드립니다.

# Clova AI Rush 2021
: AI RUSH는 Naver Clova에서 주최하는 AI 모델링 챌린지입니다.

### 참가 지원
![image](https://user-images.githubusercontent.com/59414764/122434428-0e9a3100-cfd2-11eb-8624-6413e4f85a72.png)  

위 일정처럼 자소서 서류로 1차 심사를 보고 2차로 코딩 테스트가 주어졌습니다. Kaggle이라고 해봤자, 타이타닉, 보스턴 집값 예측 기본 문제였고, 그 외 프로젝트라고 하더라도 YOLO와 기초적인 Keras CNN 모델을 
만드는 것이 전부였습니다만, 운이 좋아 서류에 붙은 것 같아요! 그리고 얼마 지나지 않아 코딩테스트가 진행되었고, 난이도는 일반 기업의 코딩테스트보다 훨씬 쉬웠습니다~


### 대회 시작 전 준비
저는 영상쪽에 집중하고 싶었던 터라 다른 고민도 하지 않고 1-3 MYBOX 이미지 분류 과제를 선택하게 되었어요. 다른 과제가 더 경쟁이 심하지 않았고, 과제를 바꿀 수 있었음에도 불구하고, 
'떨어지더라도 하고 싶은 것에 집중하자'는 생각으로 과제를 바꾸지 않았습니다. (다른 과제에 비해 1.5배 정도 경쟁이 더 치열했어요 ㅠ) 그리고 그렇게 마음 먹어서인지 떨어지고 나서 지금까지도 후회하진 않습니다.

시작하기 전에 일단 작년 참가자들의 대회 리뷰를 살펴보기 시작했습니다. Baseline, model ensemble이라는 용어도 처음 들어봤구요... 이전 참가자분들은 어떠한 실험을 했고, 어떠한 아쉬운 점이 있는지 중점으로 살펴보았습니다.
정말 후기란 후기는 다 모아 분석했어요. 어떠한 논문을 보셨는지, 어떤 모델, data augmentation을 썼는지, 어떠한 과정부터 진행하는 게 좋은지 등등...

그리고 Keras CNN 기초 서적('혼공머신')을 3번 정도 복습했던 것 같아요. (과제에서 PyTorch를 써야한다는 것을 모른 체 말이죠...)


### 대회 1주차
5.17에 OT가 이어졌고, NSML에 대해 설명을 들었습니다. 후기에서는 NSML 환경에 적응하는 것도 일이라고 했었는데 그리 힘들지는 않았던 것 같아요. 그리고 Baseline이 주어졌고, 코드가 PyTorch라는 사실을
알게 됐죠. 그리고 PM님께 Tensorflow 사용할 수 있는지 여쭤보니... 사용할 수 있지만, 여러 이유 때문에 pytorch를 사용하는 것을 권장한다고 말씀하셨죠 ㅠ

그리고 1주 동안 Baseline를 토대로 pytorch 모듈을 공부하기 시작했습니다. tensorflow 책은 기초부터 심화까지 다양했지만, pytorch는 책이 얼마 없더라고요.
일단 '3분 딥러닝 파이토치맛', 'pytorch로 배우는 딥러닝'으로 공부했습니다. Vision & AI 단체 카톡방(제가 주로 정보를 얻는 공간입니다)에서 Efficientnet이 좋다는 말이 기억났고, 찾아보니 version 2가 나왔길레
바로 모델을 가져다 썼죠. 처음 Baseline을 돌렸을 때는 0.23점이었는데, 바로 0.33점으로 올랐습니다. 뭔가 너무 거저 먹는 거 같아 불안하더라고요. 일단 교수님이 항상 말씀하시던 '알고 쓰는 게 좋아'가 떠올랐고
바로 Efficient Net에 대한 정보를 얻기 시작했습니다. Efficientnet v1은 https://www.youtube.com/watch?v=5sXQGH9I2VM 동영상으로 빠르게 정보를 얻고, v2는 논문 원서를 보면서 리뷰했죠. 나온 지 얼마 안된
따끈한 논문이었죠. 확실히 최신 기술을 먼저 접한다는 느낌이 어떤 느낌인지 알 것 같습니다 ㅎㅎ 간단하게 축약하자면, 기존 v1은 Model Scaling(Width Scaling + Depth Scaling + Resolution Scaling)을 통해
모델의 FLOPS 대비 성능을 올렸고, v2는 Progressive Learning(이미지를 학습할 때마다 더 크게 만드는 것)을 사용하여 학습 속도를 증가시켰다는 것입니다.

이렇게 공부하면서 ResNet, DenseNet, VGG net, model ensemble, data augmentation에 대해서 알 수 있었습니다. 또한 Efficient Net을 분석하면서 BatchNormalization, Silu에 대해서 알 수 있게 되었죠.
각 기능, 방법들이 어떤 식으로 작동하는 지, 그리고 어떠한 성격을 가지는 지 위주로 공부했습니다. 

그리고... 이렇게 기초부터 공부하면서, 뭔가 남들보다 늦게 시작하는 것 같아 아쉽기도 했습니다. 0.7 넘은 사람들이 수두룩했거든요.
괜히 리더 보드를 보면 우울해지는 것 같아 이때부터 안 봤던 것 같아요.


### 대회 2주차
1주차 때 배운 지식들을 가지고 Hierarchical Image Classification 모델을 만들기 시작했습니다. 뭔가 대분류를 먼저 하고, 중분류, 소분류 순서대로 분류하도록 하면 되지 않을까 생각했었는데, 역시 사람들은 생각하는 게 다 똑같았던 것 같아요. 'Hierarchical Image Classification'을 키워드로 IEEE에서 논문을 검색했고, HCNN, HD-CNN을 접할 수 있었어요. 그리고 이를 토대로 classifier를 제작하려했습니다.   

 그것보다 문제는 loss function이었어요. 한 개의 label을 분류하는 문제는 접해본 적이 있지만, Multi Label Classification은 해본 적이 없었기 때문이죠. 그리고 '모두의 딥러닝' 강의를 다시 복습하면서 어떻게 해결하는 지 찾기 시작했어요. 그리고 pytorch docs를 뒤져보며, BCELoss 또는 BCEWithLogitsLoss를 쓰면 된다는 것을 알아내었습니다. 그리고 Github에서 다른 사람들은 이 함수를 어떻게 사용하는지 검색해보았어요. 3일이란 시간이 걸리긴했지만, BCEWithLogitsLoss를 겨우겨우 사용할 수 있게 되었고, 점수를 0.46점까지 올릴 수 있었습니다. 
 뭔가 많이 이상했어요. 데이터에 문제가 없고, 모델만 올바르게 쓰면 일반적으로 정확도 80% 이상은 나올텐데 그에 비해서 터무니 없이 낮은 점수였죠. 분명 어딘가 문제가 있을 것이라 생각했습니다. classifier에 softmax를 넣고 빼기도 해보았고, Baseline코드로 되돌려 코드를 다시 짜보기도 하였어요. 해결되는 것은 없었고, 남은 1주동안 연구하는 것을 포기하고 그냥 Epoch 1000까지 돌려보자는 생각을 하기 시작했습니다. 하루동안 한 것은 validation dataset을 만들어 과적합되는 지만 살펴볼 수 있는 코드를 짠 것 뿐이었습니다. 


### 대회 3주차
포기할까 하던 와중에, Baseline에서 3계층 분류에 Cross Entropy Loss function 3개가 선언되어 있던 게 생각났어요. (하지만 Baseline 코드에서 실제적으로 계산에 사용됐던 건 1개의 loss function뿐) 이처럼 3개의 loss function을 사용하여 각각 대분류, 중분류, 소분류에 써보자는 생각을 하게 됐습니다. 그리고 더해서 'nothing'(아무것도 아님)을 뜻하는 -1 class도 중분류, 소분류 계층에 추가하였습니다. 이렇게 다시 Github와 pytorch doc을 참고하여 연구하면서 하루를 다 써 코드를 완성하였습니다. 그리고 성적은 단번에 0.81점을 기록하였어요. (아직까지도 왜 그렇게 단번에 점수가 올랐던 것인지 이해하지 못했습니다...)  

 그리고 다시 희망을 품고, 연구를 재개하였습니다. cross_entorpy_loss에서 ignore_index 기능이 있다는 것을 알아내었고, 'nothing' class를 계산하지 않도록 적용하였습니다. (평가 방법에서는 실제 -1 class를 어떤 class로 판단하여도 감점이 되지 않는 원리였고, 아무거나 비슷한 것을 찍어 점수를 높이려는 전략이었습니다) 그리고 데이터의 class 불균형 문제를 해결하기 위해 sklearn의 compute_class_weight함수를 사용하여 class weight를 계산하였고, 이를 loss function의 weight에 적용하였습니다. 그리고 feture를 혼합하거나 filter를 서로 붙이는 형식으로 model ensemble을 구현하여 적용하였죠. 기존 efficientnet v2에 rexnet을 ensemble하였고, FLOPS 제한선을 맞추기 위해 moblienet v3와 직접 만든 FCN?(C*224*224 filter, One CNN layer) 모델까지 사용하였습니다. 낮은 성능의 모델일지라도 ensemble 성능 향상에 도움이 된다는 대학원생 분의 팁이 큰 힘이 되었어요. (nfnet을 사용했을 때 점수가 가장 높았지만, 모델에 FLOPS문제가 있어 사용 금지를 당했죠...) 이러한 과정을 통해 점수는 89점까지 도달할 수 있었습니다.
 
 시도한 것들 중에 가장 희한했던 것은 계층 분류 순서를 바꾸는 것이었습니다. 기존에는 대분류 -> 중분류 -> 소분류 순서로 분류를 했었습니다만, 소분류 -> 중분류 -> 대분류 순서로 분류를 하게 해했을 때 점수가 0.93까지 올라갔어요. 제 예상대로라면 모델의 head에서 대략의 feature를 결정하고 모델이 깊어질 수록 세세한 feature를 알아내도록 하는 것이었지만, 완전 다르게 작동한 것이죠. (제가 실험 중에 모델을 워낙 희한하게 짜서 그런 것일 수도 있을 것 같네요...) 그리고 마지막으로 hyperparameter, data augmentation을 실험하고, cutmix를 구현하여 연구를 마무리할 수 있었습니다. 최종 0.93324점으로 마무리하였습니다.
 
 연구한 것 중에 한 가지 아쉬운 것이 있다면, 후에 실험하여 알게 된 것인데, cutmix가 과적합에 영향을 미친다는 것이었어요. 처음부터 cutmix를 적용하는 것보다 lr scheduler를 이용하여 일정 epoch에 cutmix를 적용하였을 때 성능이 더 좋아지는 것을 볼 수 있었습니다. 그리고 준지도 학습 모델 noisy student을 구현해보지 못한 게 아쉽게 다가오네요. noise label을 생각 못했던 것도 아쉽네요...

 
validation dataset score:  
(valid dataset의 loss는 잘못 나왔네요)     
 
 ![image](https://user-images.githubusercontent.com/59414764/122453145-fd0e5480-cfe4-11eb-8890-1be920924aee.png)


 
loss & lr:  
 ![image](https://user-images.githubusercontent.com/59414764/122453054-e405a380-cfe4-11eb-82ae-8ec168d8f693.png)



3주차 실험 내역:  
![image](https://user-images.githubusercontent.com/59414764/122453889-ad7c5880-cfe5-11eb-9330-8c8a53118b8c.png)


### 대회 결과 및 피드백, 느낀점
아쉽게도 0.0046점 차이로 2라운드에 진출하지 못했습니다. (1등은 0.9606점) 실험해보지 못한 것이 많아 많이 아쉽게 느껴지네요. PyTorch를 제대로 이해하고 시작했다면 1등을 할 수 있었을까요?
0.9333 점수가 높아보이긴 하지만, 실제 대회에서는 0.001점도 매우 크다고 들었습니다. 아직 많이 부족한 점수일 지도 모르겠네요.
semi-supervised model(noisy student), noise label, auto hyperparameter tuning module, 제대로된 model ensemble 등 아직 해보지 않은 것이 많아 너무 아쉽게 느껴집니다.

조금은 생색을 내자면(ㅋㅋㅋ) 정말 3주동안 하루(쉬는 날)를 제외하고, 점심 쯤에 일어나서 하루종일 책상에 앉아 연구하고 아침이 되면 잠들고를 반복했습니다. 결과는 아쉽지만, 큰 마음먹고 도전한 만큼, 값진 경험을 가져다 준 공모전이었습니다. 모듈에 대한 이해, 수학 지식, 모델에 대한 경험 등 부족한 것이 어떤 것인지 깨닫게 해주었고, '조금 더 공부하면 확실하게 성장할 수 있겠구나'는 생각이 드네요. 무엇보다 'AI 분야에서 일을 해도 괜찮을 것 같다'는, 직업에 대한 확신이 들었습니다. 다른 Kaggle 대회에도 참가해보고 싶네요. 가능하다면 내년에 다시 참가해볼 예정입니다🔥

+) 대회가 아쉬웠던 점은... DM을 통해 Naver AI 현업 개발자와 교류할 수 있다는 내용도 있었지만, 막상 PM님들께 메세지를 보냈을 때, 바쁘셨던 건지... 메세지를 보지 않거나, 3~5일 후에 답장이 온다는 점이 정말 아쉬웠습니다...


### 참고 논문
[1] Convolutional Network Model using Hierarchical Prediction and its Application in Clothing Image Classification
[2] CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features
[3] EfficientNetV2: Smaller Models and Faster Training
[4] ImageNet: A Large-Scale Hierarchical Image Database
[5] Size Matters
[6] Meta Pseudo Labels
[7] High-Performance Large-Scale Image Recognition Without Normalization
[8] An overview of gradient descent optimization algorithms
[9] SELF: LEARNING TO FILTER NOISY LABELS WITH SELF-ENSEMBLING
[10] VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION
[11] HD-CNN: Hierarchical Deep Convolutional Neural Networks for Large Scale Visual Recognition
[12] 효율적인 사물 이미지 분류를 위한 계층적 이미지 분류 체계의 설계 및 구현
