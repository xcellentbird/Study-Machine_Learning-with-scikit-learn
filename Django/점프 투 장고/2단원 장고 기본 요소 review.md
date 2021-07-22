장고, 백엔드를 공부하게 된 계기를 상기할 겸, 다시 설명하자면, 후에 머신러닝 모델이나 데이터 처리는 대부분 백엔드에서 이루어진다. ~~(스마트폰도 충분히 가능할 것 같은데... 아직까지 Edge 기기 머신 러닝 모델에 대한 미련을 놓지 못했다)~~ 그리고 장고를 선택한 이유는 개인적으로 Python 언어에 익숙한 상태라 빠르게 배울 수 있기 때문이다.

점프 투 장고의 2장은 '장고의 기본 요소 익히기!'다. 이 책을 통해서 간단한 게시판 앱과 서버를 만들어보았다. ~~내용은 무시해주세요~~
![](https://images.velog.io/images/xcellentbird/post/67b7f70f-524c-47fe-a787-a74fa2ecd3dc/image.png)

오늘은 이 글을 쓰면서, 복습도 하면서 기본기를 정리하고, 어떻게 프로젝트에 응용하면 좋을지 구상해볼까 한다.

# Django Intro
![](https://images.velog.io/images/xcellentbird/post/0cac143c-ee82-4c8e-a1c4-c92b5b29d50d/image.png)
장고는 다음 그림과 같이 동작한다. 일단 User로부터 '127.0.0.1/port_num/request/...'와 같이 request가 오면 프로젝트의 urls.py에서 해당 request를 어느 앱의 어느 View에서 처리할 지 Mapping해준다. 

만든 장고 프로젝트에서는 ip_address/8000/pybo/2와 같이 request가 들어오면, urls.py에서 해당 request를 분석하여 해당 앱의 view.py에 위치한 함수를 파라미터와 함께 전달하면서 실행하도록 만든다.

그리고 view에 연결된 Model.py(DB 관리, 해당 프로젝트에서는 ORM사용)와 template(웹페이지 html, css 등을 관리)에서 데이터를 처리하고 불러와 시각화하는 역할을 수행한다.

그 외로도 forms.py을 통해 특정 폼을 관리하고, admin.py를 통해 관리자 모드에서 어떤 것을 관리하고 시각화할 지 설정할 수 있다.

프로젝트 파일에 위치한 settings.py를 통해 debug 모드, template와 static(이곳에서 주로 bootstrap이나 css파일을 위치시킨다.)의 경로 설정, 사용 언어를 설정하고 관리할 수 있다.

# urls.py
해당 프로젝트에선 어떠한 request를 받을 수 있도록 되어있을까?
먼저 프로젝트 경로의 urls.py를 먼저 살펴보겠다.
## 코드 설명
![](https://images.velog.io/images/xcellentbird/post/675d0044-f72c-42c0-953d-0ddc920b3912/image.png)
'admin/' request가 오면 관리자 urls(admin.site.urls)을 연결해준다. 그리고 'pybo/~~'가 오면 일단 'pybo.urls'(pybo앱의 urls 폴더)를 매핑하도록 되어있다.

![](https://images.velog.io/images/xcellentbird/post/6bfb42b7-a9ff-4615-bfc2-8e99e6eb5e94/image.png)
프로젝트의 urls.py에서 path('pybo/', include('pybo.urls'))에 의해, pybo앱의 urls에서 request를 건너받는다.

```python
app_name = 'pybo'
```
와 같이 되어 있어, 다른 폴더에서 앱의 경로를 타이핑하지 않아도 'pybo:'와 같이 명칭을 사용하여 간편하고 다른 앱과 혼동되지 않도록 앱의 기능을 사용할 수 있게 해준다.

## 정리 및 예시

```python
path('answer/create/<int:question_id>/', 
	views.answer_create, name='answer_create')
```
예시로 윗 코드만 분석을 해보자. 

일단 ipAddress/portNum/pybo/answer/create/int형숫자'와 같은 request를 프로젝트에서 받으면 '~/pybo/~'를 인식하고, pybo앱의 urls에 request를 넘겨주게 된다. 그 후, 'answer/create/~'를 인식하여 views의 answer_create함수에 ~/int형 숫자' 파라미터와 함께 request를 요청하게 된다. 그리고 별명(name)을 설정하여, template에서 별명으로 아래와 같이 쉽게 접근 가능하도록 만들 수 있다. ('pybo:'는 앞에 설명했던 app_name이다.)
```html
<form action="{% url 'pybo:answer_create' question.id %}" method="post" class="my-3">
```

## Django API 설명
- django.url.path 
: route를 받아 view와 연결시켜준다. [[참고]](https://docs.djangoproject.com/ko/3.2/ref/urls/#django.urls.path)
```python
path(route, view, kwargs=None, name=None)
```
> **라우트(route)는 무엇일까?**
먼저 라우팅(routing)은 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정을 뜻한다. 그리고 그 경로를 route라고 한다.

- django.url.include 
: 다른 URL conf(구성)을 포함(연결)시킨다. url pattern list를 한꺼번에 넣을 수도 있다.
```python
include(module, namespace=None)
include(pattern_list)
include((pattern_list, app_namespace), namespace=None)
```

# models.py
**모델**이란 부가적인 메타데이터를 가진 **데이터베이스의 구조(layout)**를 말하며, models.py는 모델을 선언하고, 데이터를 관리해주는 역할을 한다.

models.py에서는 model을 어떻게 선언하고 관리하는 걸까?
일단, 나는 책대로 SQL을 사용하지 않고 Djnago ORM을 사용해보기로 하였다.
복습 차원에서 간단하게 ORM을 설명하자면, query문을 작성하지 않고 간편하게 모델을 구성할 수 있다는 특징이 있다. (자세한 것은 [ORM과 DBMS](https://velog.io/@xcellentbird/Database-RDBMS%EC%99%80-ORM) 글 참고)
## 코드 설명
![](https://images.velog.io/images/xcellentbird/post/10e9bdc0-5925-405c-a2da-7fddd4caed45/image.png)
위 영상과 같이 models.model을 상속받은 class를 통해 모델을 만들고, Field를 지정하여 칼럼을 만들 수 있다. 

### fields
#### Relational Field - [Django Model Relational Field](https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields.related)
'ForeignKey'는 ManyToOne Relational Field(일대다 관계형 필드)로 다른 모델과 연결(mapping)시켜주는 field다. 한 Question 모델에 여러 Answer 모델이 연결된다. on_delete를 models.CASCADE로 설정하면, Question 모델이 사라질 경우 이어져있는 Answer 모델도 사라진다.

다른 Relational Field로는 'ManyToManyField', 'OneToOneField'도 있다.
~~딱 봐도 이 아이들은 어떤 필드인지 알 수 있게 되어있다.~~

#### Data Field - [Django Model Field types](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)
> **models에는 어떤 Field들이 있을까?** 
* IntegerField - 정수
* BinaryField - bytes, bytearray
* BooleanField - bool형 (True, False)
* CharField - string형
* DateTimeField - python의 datetime.datetime. 주로 django.utils의 timezone.now()를 많이 사용한다.
* EmailField - EmailValidator로 검증 가능한 문자열 데이터
* FileField - 파일 [[참고]](https://docs.djangoproject.com/en/3.2/ref/models/fields/#filefield)
* FilePathField - 파일 경로(str로 된 경로 형식. 주로 os.path를 사용한다.)
* FloatField - float형
* ImageField - FileField를 상속받은 형태로 width, height 정보를 추가적으로 저장한다.
* GenericIPAddressField - '192.0.2.30'나 '2a02:42fe::4' 같은 IPv4, IPv6 address를 담는다. 
* JSONField - python의 dictionary 형태의 데이터
* TextField - CharField와 비슷하나 긴 string 데이터에 유용하다.
* SlugField - 유효한 URL을 위한 TextField [(Django에서 slug란 무엇인가?)](https://itmining.tistory.com/119)
* URLField - URLValidator로 검증 가능한 문자열 데이터
* UUIDField - UUID는 128 bit의 범용고유식별자(ID)이다. ex)550e8400-e29b-41d4-a716-446655440000 [[참고: UUID Wiki]](https://ko.wikipedia.org/wiki/%EB%B2%94%EC%9A%A9_%EA%B3%A0%EC%9C%A0_%EC%8B%9D%EB%B3%84%EC%9E%90)

### Model Instance  

<p>'__str__'은 표기되는 모델 데이터 이름을 설정하기 위해 사용한 함수다. 코드에서는 'subject'를 이름으로 데이터를 표기하기 위해 설정해놓았다.</p>

그 외로도 많은 모델 인스턴스들이 있다. - [Model Instance Reference](https://docs.djangoproject.com/en/3.2/ref/models/instances/#model-instance-reference)

+) 그 외로도 아래 코드와 같이 meta 옵션도 사용 가능하다. - [Model Meta Options]
(https://docs.djangoproject.com/en/2.1/ref/models/options/) 참고 ~~아직 배우지 않았으니 자세한 것은 넘어가도록 하겠다~~
```python
class Test(Models.Mode):
    pass

    class Meta:
        pass
```

# views.py
위에서 설명했다시피, view는 url로부터 request를 받고, request에 해당하는 함수 또는 클래스를 이용하여 모델과 템플릿(html)을 연결하고 request를 처리해준다.

+) views.py는 클래스형 뷰(CBV)와 함수형 뷰(FBV)로 나뉜다. FBV(Function-Based Views)는 간편하나 확장 및 재사용이 어렵다는 점이 있고, CBV(Class-Based Views)는 코드 구조가 깔끔하고, class의 이점 답게 코드 재사용 및 확장에 용이하다. [[참고 블로그]](https://velog.io/@yejin20/DjangoFBV-%EC%99%80-CBV) 큰 기능 차이는 없는 듯하다. 본 프로젝트에서는 FBV 방식으로 views 코드를 구성하였다.

## 코드 설명
views.py 코드는 양이 많아 2개의 함수만 리뷰하도록 하겠다.
![](https://images.velog.io/images/xcellentbird/post/fb15f0b8-27eb-4c6e-b332-baf71e795056/image.png)
아래 urls.py 코드들을 통해 'ipAddress/postNum/pybo/' URL로 요청이 들어오면 위의 views.index함수가 실행된다.
```python
path('pybo/', include('pybo.urls'))
path('', views.index, name='index')
```

그리고 'Question.objects.order_by('-create_date')'를 통해 Question모델의 객체들(objects)을 불러와 create_date 기준 역순으로 정렬시킨다. create_date 앞에 마이너스(-) 부호를 붙여줬기 때문에 역순으로 정렬된다.
그렇게 만든 question_list를 context이름의 dictionary형태로 만들고, render함수를 통해 요청에 응답하도록 한다.

두번째로 리뷰할 함수는 아래 이미지와 같다.
![](https://images.velog.io/images/xcellentbird/post/3ef7119a-7458-4a60-80a0-151c1a2c7d47/image.png)

get_object 함수를 통해 question_id에 해당하는 모델 데이터를 'question' 이름으로 불러온다.

요청의 HTTP Method가 POST일 경우, AnswerForm객체에 담아 save함수를 통해 'answer'라는 새로운 DB 객체를 만들고 저장한다. 그리고 날짜와 내용을 설정하고 save(참고:[ModelForm.save() method](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method))를 통해 DB를 저장한다.

마지막으로 redirect를 통해 'pybo:detail'에 해당하는 URL request를 question_id를 포함하여 실행시켜준다.

## Django API 설명

- django.shortcuts.render() : 해당 request에 대해 template과 context를 연결짓고, HttpResponse 객체로 반환한다. (그렇다면 HttpResponse는 어떠한 원리로 작동할까? 참고: [Django Request and Response](https://docs.djangoproject.com/en/3.2/ref/request-response/#module-django.http), [Django Github](https://github.com/django/django/blob/65b880b7268dd8fe97fde5af77bede46305eb499/django/http/response.py#L89) - 다음 글로 코드 리뷰 해봐야겠다.)
```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

- django.shortcuts.get_object_or_404() : get과 같이 모델의 id에 해당하는 데이터를 가져온다는 점에서 비슷하지만, id에 해당하는 모델 데이터가 없을 때, Http404 에러를 일으킨다는 차이점이 있다.
```python
get_object_or_404(klass, *args, **kwargs)
```
- django.shortcuts.redirect() : 파라미터와 함께 URL request를 일으킵니다. URL과 함께 ttpResponseRedirect을 반환하는 원리로 작동한다. - 참고: [django.shortcuts.redirect](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#redirect)
```python
redirect(to, permanent=False, *args, **kwargs)
```

---
# 리뷰를 마치며.
form이나 html, css, bootstrap 등 리뷰를 못해본 부분이 많다. 이러한 부분들은 프론트엔드 웹에 더 가깝다고 생각했고, 아쉽게도 나는 모바일 앱이나 머신러닝 모델의 서빙을 위해 백엔드가 필요했기 때문에, 관련 내용만 깊게 리뷰를 해보았다.

이렇게 리뷰를 해보면서 장고의 기본기에 대해서 조금은 더 깊게 이해할 수 있었고, 지금 진행하고 있는 프로젝트에서 어떻게 서버를 구축할 수 있을까에 대해 많은 힌트를 얻어가는 것 같다.

CS지식, 특히 네트워크 부분에 대해 더 공부하고, 장고를 배움과 동시에 해당 네트워크 지식이 어떻게 쓰이는지 알아갈 수 있을 것 같다.

리뷰에 리뷰를 하다보니 배우고 글을 써봐야할 것들이 더 많아졌다.
> Self 질문 리스트:
* HTTP와 HTTPS의 차이는 알고 있지만, 백엔드 프레임워크에서는 어떻게 응용되고 있을까?
* HTTPResponse 함수의 작동 원리 파헤치기
* HTTP Method와 REST API [[참고 예정 블로그]](https://meetup.toast.com/posts/92)
* URI와 URL
* IPv4와 IPv6

이와 같은 질문들에 대해 답하고 나면(~~너무 깊게 빠지지만 말자~~) 더 실력이 올라갈 것이라 생각한다.

나는 남들처럼 매일 TIL(Today I Learned) 글을 쓰는 것보다는, 일단 꾸준하게 작업하며 프로젝트를 끝내고, 하루동안 한꺼번에 배운 지식들을 정리해서 글을 쓰는 게 나에게 더 잘 맞는 방법인 것 같다. 하나의 일에만 집중해야 학습 효율이 크다. ~~사용 효율은 좋지만 한번에 하나씩 밖에 처리 못하는 CPU처럼...~~ 복습하고 정리하기 위해 글을 쓰기로 마음먹었지만, 남들 눈에는 어떻게 보일지도 궁금하다. 읽는 사람이 있다면 부디 좋게 봐줬으면 하는 바람이다.

다음 계획은
1. 서버 AWS Cloud에 올려 온라인 상태 유지시키기
2. 서빙 받은 이미지를 서버의 DB(ORM)에 저장하고, 학습 파이프라인 제작하기
3. 코틀린과 안드로이드: 이미지와 딥러닝 모델 서빙 앱 제작하기
4. 학습된 모델을 앱으로 서빙하기
