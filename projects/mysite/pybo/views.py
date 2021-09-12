from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm

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

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # 답변을 저장하는 2가지 방법
    # 첫번째 방법
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 두번째 방법
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # redirect = 답변을 생성한 후 질문 상세 화면을 다시 보여주기 위함 / 페이지 이동을 위한 함수
    # detail 별칭은 question_id가 필요하므로 question.id를 인수로 전달
    answer.save()
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)