from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200) # 질문의 제목 (최대 200자)
    content = models.TextField() # 질문의 내용
    # TextField = 글자수 제한 없음
    create_date = models.DateTimeField() # 질문을 작성한 일시
    # DateTimeField = 날짜와 시간에 관계된 속성

    def __str__(self): # id 값 대신 제목을 표시할 수 있다
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문 (어떤 질문의 답변인지 알기 위함), Question 모델을 속성으로 가져감
    # ForeignKey = 기존 모델을 속성으로 연결하기 위함
    # on_delete=models.CASCADE = 이 답변과 연결된 질문(Question)이 삭제 될 경우 답변(Answer)도 함꼐 삭제된다
    content = models.TextField() # 답변의 내용
    create_date = models.DateTimeField() # 답변을 작성한 일시
