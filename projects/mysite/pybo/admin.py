from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin): # 모델 검색 기능
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)