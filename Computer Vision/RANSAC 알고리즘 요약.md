참고: <다크 프로그래머> https://darkpgmr.tistory.com/61

# RANSAC

## RANSAC의 필요성
1) 주로 데이터들은 최소자승법을 이용하여 오차를 최소화하는 모델(파라미터)를 찾는다.

![image](https://user-images.githubusercontent.com/59414764/113492671-0c1c5500-9514-11eb-8328-454885d65b5c.png)


2) 데이터들은 보통 선형을 이루지 않는다.

![image](https://user-images.githubusercontent.com/59414764/113492676-26eec980-9514-11eb-8d30-670670ae2867.png)


3) 일부 데이터 집합은 큰 노이즈에 의해 outlier(이상점)이 되어 최적의 모델을 찾는데 방해가 된다.

![image](https://user-images.githubusercontent.com/59414764/113492701-5998c200-9514-11eb-9f17-2cf72b5689db.png)


=> 이러한 경우에 쓰이는 것이 RANSAC(RAndom SAmple Consensus: 무작위 샘플 일치 정도)이다.

![image](https://user-images.githubusercontent.com/59414764/113492726-91076e80-9514-11eb-9919-5847925c1f00.png)


## RANSAC의 원리와 알고리즘
1) 준비: 무작위 데이터 샘플 세트(최소 3개의 샘플)를 만든다.
2) 실행: 뽑은 샘플 세트만을 이용하여 모델(최소자승법과 같은 포물선)을 만든다.
3) 평가: 전체 샘플들이 만든 모델과 얼마나 일치하는지(점수 = 일치(모델과 일정 거리 안으로 떨어져있는)하는 샘플 개수) 평가한다.
4) 반복: 1)준비 단계부터 N번 다시 시작한다.
5) 결과: 가장 점수가 높았던 모델을 최종으로 삼는다.


## RANSAC의 활용
local feature matching, Visual Odometry, Scene Matching, Optical Flow 등등


## RANSAC 알고리즘의 파라미터
(N:반복횟수, m:한번에 뽑는 샘플 개수, a:전체에서 inlier의 비율, p:RANSAC 성공확률)

![image](https://user-images.githubusercontent.com/59414764/113492997-b0070000-9516-11eb-883b-408677244f70.png)

## RANSAC의 특징
1. RANSAC은 수확적 확률일 뿐이므로 결과가 매번 달라질 수 있다.
2. N을 늘려도 완벽한 결과를 못 찾을 수 있다.
3. outlier들이 무작위로 분포하지 않고, 특정한 structure를 이룬다면 예상하지 않은 모델이 나올 수 있다.

## 그 외의 알고리즘
![image](https://user-images.githubusercontent.com/59414764/113493056-3885a080-9517-11eb-82ac-09d5b25aa71c.png)
