from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name = 'index'),
    path('<int:resume_id>/', views.detail, name='detail'),
    path('<int:resume_id>/result', views.result, name='result'),
]