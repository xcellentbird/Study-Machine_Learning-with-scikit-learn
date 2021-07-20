from django.contrib import admin
from .models import Question

# Admin에서 검색가능하도록 설정


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


# models의 Question모델을 Admin에 등록한다.
admin.site.register(Question, QuestionAdmin)
