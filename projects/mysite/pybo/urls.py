from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('question/create/', ...) # 최종 매핑되는 URL은 pybo/question/create/ 가 된다. (config/urls.py + pybo/urls.py)
]