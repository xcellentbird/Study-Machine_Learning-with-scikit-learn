## 02-2
Django는 SQL 대신 ORM(object relational mapping)기능을 사용하여 DB를 관리할 수 있다. *(그렇다면 SQL(Query)과 ORM은 어떠한 차이점이 있으며, 어떤 환경, 프레임워크를 사용할까?)*

Django에서는 테이블을 생성하기 위해 migrate 명령을 사용해야 하며, 그 전에 테이블 작업 파일을 불러오기 위해 makemigrations 명령을 먼저 사용해야 한다. ![](https://images.velog.io/images/xcellentbird/post/a2d44764-ab1d-4f24-8095-ca91543420e1/image.png)


#### 모델 사용법
- 데이터 생성 및 저장
```python
d = 모델A(모델속성=데이터,...)
d.save()
```
- 데이터 id값 확인
```python
d.id
```
- 데이터 모두 조회하기
```python
모델A.objects.all()
```
- 데이터 리스트, 조건으로 조회하기
```python
# 해당 id의 데이터가 존재하면 빈 list가 반환된다
모델A.objects.filter(id=아이디_번호)
```
- 데이터 하나만 조회하기
```python
모델A.objects.get(id=아이디_번호)
```
- 제목 일부를 이용한 데이터 조회하기
```python
모델A.objects.filter(모델속성__contains=데이터 일부)
```
- 데이터 수정하기
```python
d.모델속성 = 변경할 데이터
d.save()
```
- 데이터 삭제하기
```python
d.delete()
```
- 연결 데이터 조회하기
```python
d.연결모델명_set
```

## 02-4
다음과 같이 order_by를 사용하여 데이터를 정렬하여 가져올 수 있다.
```python
data_list = modelA.objects.order_by('모델속성')
```
역순으로 정렬하여 가져오고 싶을 땐 모델속성에 마이너스 부호(-)를 앞에 넣어주면 된다.
```python
data_list = modelA.objects.order_by('-모델속성')
```
render함수는 다음과 같이 사용할 수 있다.
>django.shortcuts.render(request, template_name, context=None)
> * request: 응답할 request 객체
> * template_name: 템플릿 이름
> * context: dictionary 타입의 데이터  
> [Reference](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#render)

템플릿 태그 정리
- 조건문
```html
{% if 조건문1 %}
	<p>...</p>
{% elif 조건문2 %}
	<p>...</p>
{% else %}
	<p>...</p>
{% endif %}
```
- 반복문
```html
{% for item in list %}
	<p>순서: {{ forloop.counter }}</p>
	<p>{{ item }}</p>
	<p>{{ item.속성 }}</p>
{% endfor %}
```
존재하지 않음(404)페이지 출력하기
modelA.objects.get(id=...)대신에 get_object_or_404(modelA, pk=...)을 대입하여 존재하지 않은 페이지 접근에 대해 404페이지로 대처할 수 있다.
>django.shortcuts.get_object_or_404(klass, *args, **kwargs)  
>[Reference](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#get-object-or-404)

### 오늘의 결과 화면
![](https://images.velog.io/images/xcellentbird/post/9a95f76b-60eb-4367-9414-4dceb76588a6/image.png)
![](https://images.velog.io/images/xcellentbird/post/cfc6909f-a1fe-4354-a92c-30935ef5e2f6/image.png)
