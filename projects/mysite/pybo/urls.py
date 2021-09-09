from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    # path('question/create/', ...) # 최종 매핑되는 URL은 pybo/question/create/ 가 된다. (config/urls.py + pybo/urls.py)
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]