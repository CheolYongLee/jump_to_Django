from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context) # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    # 없는 데이터를 요청 할 경우 500 오류 페이지가 아닌 "Not Found (404)" 페이지를 리턴하는 함수
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)