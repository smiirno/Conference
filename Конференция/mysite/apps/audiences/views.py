from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from .models import Audience, Lecture


def index(request):
    audiences_list = Audience.objects.order_by('audience_number')
    lectures_list = Lecture.objects.order_by('audience')

    if request.method == 'POST':
        audience = request.POST.get('audience')
        lecture_title = request.POST.get('lecture_title')
        speaker_name = request.POST.get('speaker_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        a = Lecture(audience=audience,
                    lecture_title=lecture_title,
                    speaker_name=speaker_name,
                    start_time=start_time,
                    end_time=end_time)

        a.save()

        return redirect('')
    else:
        return render(request, 'audiences/list.html', {'audiences_list': audiences_list, 'lectures_list': lectures_list})


def lectures(request):
    audiences_list = Audience.objects.order_by('audience_number')
    lectures_list = Lecture.objects.order_by('audience')
    return render(request, 'audiences/lectures.html', {'audiences_list': audiences_list, 'lectures_list': lectures_list})
