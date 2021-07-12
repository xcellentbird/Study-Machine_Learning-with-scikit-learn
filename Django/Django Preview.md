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

---   
## Django의 MVT Pattern
MVT = Model, View, Template

<img src="https://user-images.githubusercontent.com/59414764/125022236-2a679300-e0b7-11eb-9f45-bf3556a0a716.png" width="750" height="400" />

1. User로부터 어떠한 요청이 들어오면,
2. URL에서 요청을 해석하여, View와 연결.
3. View에서는 들어온 요청을 Model, Template를 통해 처리한다.
4. Model에서는 DB(데이터 베이스)를 ORM(Object Related Model)구조로 관리하는 역할을 한다.
5. Template에서는 HTML + template언어를 사용하여 UI를 관리하는 역할을 한다.

---   
## View

1. 일단 setting.py에서 application 목록에 만든 앱을 추가하여 매니저에서 앱으로 인식할 수 있도록 만든다.   
<img src="https://user-images.githubusercontent.com/59414764/125004257-1e1e0e80-e094-11eb-89db-b38efc05daa3.png" width="500" height="300" />

2. App의 view.py를 다음과 같이 작성하여 'hello world!'띄우도록 만든다.   
<img src="https://user-images.githubusercontent.com/59414764/125004608-dba90180-e094-11eb-9425-70e89a6f4caf.png" width="300" height="100" />

- index 함수의 경우, 'requset' 요청을 받아 실행된다.
- HttpResponse() [참고](https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.HttpResponse) 는 조금 더 공부해봐야할 것 같다.

3. urls.py에서 다음과 같이 작성하여 '127.0.0.1/<port_num>/' 라는 요청이 들어왔을 때, app/views의 index함수가 실행되도록 한다.   
<img src="https://user-images.githubusercontent.com/59414764/125020930-aca28800-e0b4-11eb-9319-e52dc1b25eaa.png" width="300" height="300" />

4. 127.0.0.1/<port_num> 에 접속하면 다음과 같은 페이지를 볼 수 있다.
<img src="https://user-images.githubusercontent.com/59414764/125021341-6568c700-e0b5-11eb-915d-04df9510a69b.png" width="280" height="70" />

---   
## Admin User

1. urls.py에는 다음과 같이 '127.0.0.1/port/admin' 요청이 들어오면 django.contrib의 admin.site.urls(서버의 관리자 페이지)에 접근할 수 있게 되어있다
<img src="https://user-images.githubusercontent.com/59414764/125021640-09eb0900-e0b6-11eb-8ab0-efefeb2a1326.png" width="250" height="130" />
   
2. 아래 명령어를 통해 migration(모델의 변경 사항을 저장하는 작업, 테이블을 생성하는 작업)한다.
```
$ python manage.py migrate
```

3. 아래 명령어를 통해 superuser(관리자) 계정을 생성합니다. (아래 빨간 글씨의 경우, 비밀번호가 너무 짧다는 경고를 의미).  
```
$ python manage.py createsuperuser
```
<img src="https://user-images.githubusercontent.com/59414764/125022792-6d763600-e0b8-11eb-9538-87bf5e8448d2.png" width="500" height="150" />.  

4. '/admin' 요청을 통해 로그인 페이지에 접속하여 설정한 ID와 password를 입력하면, 관리자 페이지에 접속할 수 있게 된다.
![image](https://user-images.githubusercontent.com/59414764/125023077-102eb480-e0b9-11eb-944e-0e065580ca7f.png)
   
![image](https://user-images.githubusercontent.com/59414764/125023154-3b190880-e0b9-11eb-96a8-f3951a7859b4.png)

---   
## Models
   
1. 아래 그림과 같이 models.py를 이용하여 ORM(SQL과 같이 Relational DataBase에 속한다) 객체를 만들 수 있다.
<img src="https://user-images.githubusercontent.com/59414764/125252919-dae1cb00-e333-11eb-89d3-86c414d0eb9c.png" width=500 height=400 />
   
2. admin.py에 ORM객체를 등록하여 관리자 모드에서 모델을 관리할 수 있게 한다.
<img src="https://user-images.githubusercontent.com/59414764/125250433-365e8980-e331-11eb-817d-c441970debdf.png" width=350 height=100 />
   
3. 'makemigrations' 명령어를 통해 장고가 테이블 작업을 수행하기 위한 파일들을 생성한다. 그 후에 'migrate' 명령어를 통해 테이블이 생성된다.
```
python manage.py makemigrations
python manage.py migrate
```
<img src="https://user-images.githubusercontent.com/59414764/125249914-ad475280-e330-11eb-8bd7-ba2783cc5888.png" width=400 height=100 />

4. 다음과 같이 관리자 페이지에 접속하여 ORM객체를 만들거나 변경할 수 있게 된다.
<img src="https://user-images.githubusercontent.com/59414764/125254847-d3232600-e335-11eb-8f33-091b4f372018.png" width=700 height=200 />

---
## Models to Template, Template to Models

1. python은 html을 그냥 인식할 수 없기 때문에, 아래 그림과 같이 settings.py에서 DIRS에 template의 경로를 넣어주어야 한다. 'BASE_DIR'는 settings.py 위쪽에 프로젝트 경로가 선언되어있다.
<img src="https://user-images.githubusercontent.com/59414764/125273850-4fbf0000-e348-11eb-87b6-c7d401df8c22.png" width=350 height=100 />

2. forms.py파일을 만들고 데이터를 입력 받기 위한 form 클래스를 만든다. 그리고 Meta 클래스를 만들어 어떤 모델의 어떤 칼럼과 연결되어 있어있는지 지정해놓는다.
<img src="https://user-images.githubusercontent.com/59414764/125275658-4767c480-e34a-11eb-82b8-ec6ded8a874d.png" width=400 height=150 />

3. views.py에는 view함수를 다음 그림과 같이 만든다. 여기에서 중요한 점은 POST를 통해서 데이터를 받아온다는 것과 render함수를 통해 template와 이어주고, dictionary형태로 template에 정보를 보낼 수 있다는 것이다.
<img src="https://user-images.githubusercontent.com/59414764/125274886-58fc9c80-e349-11eb-98d8-6238ef262a0d.png" width=400 height=100 />

4. urls.py에서 views의 view함수를 어떤 명령이 들어왔을 때 보여줄 지 설정해놓는다.
<img src="https://user-images.githubusercontent.com/59414764/125275245-c01a5100-e349-11eb-8325-5900d8d60059.png" width=350 height=100 />

5. coffee.html은 다음과 같이 form 형태로 POST를 method로 지정하여 모델을 불러오거나 submit type의 버튼을 통해 view에 모델을 보낼 수도 있다.
<img src="https://user-images.githubusercontent.com/59414764/125276136-d5dc4600-e34a-11eb-8e41-7946f60f12f1.png" width=400 height=400 />

6. 다음과 같이 Template(xml)과 Modle(관리자 페이지)에 적용이 되는 결과를 확인할 수 있다.
<img src="https://user-images.githubusercontent.com/59414764/125276094-c5c46680-e34a-11eb-87d3-286be8262397.png" width=200 height=400 />
<img src="https://user-images.githubusercontent.com/59414764/125276595-5ef37d00-e34b-11eb-9132-6a47129878bc.png" width=600 height=400 />
