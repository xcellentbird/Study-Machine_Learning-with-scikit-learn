## Django 설치
1. venv 가상 환경 만들기
```
$ python3 -m venv dj-preview
$ source bin/activate
```

2. django 설치
![image](https://user-images.githubusercontent.com/59414764/124951984-d2954180-e04e-11eb-902c-616d2bb281e0.png)

3. 프로젝트 생성
```
$ django-admin startproject <project_name>
$ cd <project_name>
$ python3 manage.py runserver
```
![image](https://user-images.githubusercontent.com/59414764/124990067-d8088100-e07a-11eb-916b-a64fab8046c1.png)
   
4. 설치 및 프로젝트 생성 성공 화면.  
<img src="https://user-images.githubusercontent.com/59414764/124990222-08501f80-e07b-11eb-8289-e7977f6accca.png" width="500" height="500" />

5. App 생성
```
$ django-admin startapp <app_name>
```

## Django의 MVT Pattern
MVT = Model, View, Template

1. User로부터 어떠한 요청이 들어오면,
2. URL에서 요청을 해석하여, View와 연결.
3. View에서는 들어온 요청을 Model, Template를 통해 처리한다.
4. Model에서는 DB(데이터 베이스)를 ORM(Object Related Model)구조로 관리하는 역할을 한다.
5. Template에서는 HTML + template언어를 사용하여 UI를 관리하는 역할을 한다.

## View

1. 일단 setting.py에서 application 목록에 만든 앱을 추가하여 매니저에서 앱으로 인식할 수 있도록 만든다.   
<img src="https://user-images.githubusercontent.com/59414764/125004257-1e1e0e80-e094-11eb-89db-b38efc05daa3.png" width="500" height="300" />

2. App의 view.py를 다음과 같이 작성하여 'hello world!'띄우도록 만든다.   
<img src="https://user-images.githubusercontent.com/59414764/125004608-dba90180-e094-11eb-9425-70e89a6f4caf.png" width="600" height="200" />


