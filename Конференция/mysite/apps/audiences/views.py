from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Audience, Lecture


def index(request):
    audiences_list = Audience.objects.order_by('audience_number')
    return render(request, 'audiences/list.html', {'audiences_list': audiences_list})


def detail(request, audience_number):
    try:
        a = Audience.objects.get(number=audience_number)
    except:
        raise Http404('Страница не найдена')

    return render(request, 'audiences/detail.html', {'audience': a})
