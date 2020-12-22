from django.urls import path

from . import views

app_name = 'lecture'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:audience_id>/', views.lectures, name='lectures'),
    path('<int:audience_id>/add_lecture/', views.add_lecture, name='add_lecture')
]
