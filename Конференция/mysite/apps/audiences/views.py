from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Audience, Lecture


def index(request):
    audiences_list = Audience.objects.order_by('audience_number')
    lectures_list = Lecture.objects.order_by('audience')
    return render(request, 'audiences/list.html', {'audiences_list': audiences_list, 'lectures_list': lectures_list})


def detail(request, audience_number):
    try:
        a = Audience.objects.get(number=audience_number)
    except:
        raise Http404('Страница не найдена')

    return render(request, 'audiences/detail.html', {'audience': a})
