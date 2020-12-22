import time

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import Lecture, Audience


def index(request):
    lectures_list = Lecture.objects.order_by('start_time')
    audiences_list = Audience.objects.all()

    return render(request, 'lectures/list.html', {'lectures_list': lectures_list, 'audiences_list': audiences_list})


def lectures(request, audience_id):
    try:
        lectures = Lecture.objects.get(id=audience_id)
    except:
        raise Http404("Аудитория не найдена")

    return render(request, 'lectures/lectures.html', {'lectures': lectures})


def add_lecture(request, audience_id):

    lecture_title = request.POST.get('lecture_title')
    speaker_name = request.POST.get('speaker_name')
    description = request.POST.get('description')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    a = Lecture(audience_number=audience_id,
                lecture_title=lecture_title,
                speaker_name=speaker_name,
                description=description,
                start_time=start_time,
                end_time=end_time)

    a.save()

    return HttpResponseRedirect(reverse('lecture:lectures', args=( a.id )))
