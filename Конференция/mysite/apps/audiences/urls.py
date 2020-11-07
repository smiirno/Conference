from django.urls import path

from . import views

app_name = 'audiences'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:audience_number>/', views.detail, name='detail')
]