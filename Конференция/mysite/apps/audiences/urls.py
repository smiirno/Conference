from django.urls import path

from . import views

app_name = 'audiences'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_lectures/', views.lectures, name='lectures')
]
