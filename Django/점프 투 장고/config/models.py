from django.db import models
# Django의 ORM은 쿼리문을 몰라도 데이터 작업을 할 수 있다는 장점이 있다.
# 참고로 'makemigrations','migrate'명령은 모델의 속성이 추가되거나 변경된 경우에 실행되는 명령이다. 메서드만 추가된 것일 땐 생략가능하다.


class Question(models.Model):
  # 연결모델명_set 방법으로 연결된 데이터(여기에서는 Answer)를 조회활 수 있다.
    def __str__(self):
        return self.subject
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    # 다른 모델의 속성으로 갖기 위해 ForeignKey를 쓴다. 여기에서 on_delete=models.CASCADE로 설정하면 답변에 연결된 질문이 삭제되면 답변도 함께 삭제시킬 수 있다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
