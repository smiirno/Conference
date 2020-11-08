from django.urls import path
from .models import Audience, Lecture

from . import views

app_name = 'audiences'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:audience_number>/', views.detail, name='detail')
]