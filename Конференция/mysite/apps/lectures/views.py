from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from .models import Lecture


def index(request):
    lectures_list = Lecture.objects.order_by('audience_number')
    audiences_list = Lecture.objects.get('audience_number')

    # if request.method == 'POST':
    #     audience_number = request.POST.get('audience')
    #     lecture_title = request.POST.get('lecture_title')
    #     speaker_name = request.POST.get('speaker_name')
    #     start_time = request.POST.get('start_time')
    #     end_time = request.POST.get('end_time')
    #
    #     a = Lecture(audience_number=audience_number,
    #                 lecture_title=lecture_title,
    #                 speaker_name=speaker_name,
    #                 start_time=start_time,
    #                 end_time=end_time)
    #
    #     a.save()
    #
    #     return redirect('')
    # else:
    return render(request, 'lectures/list.html', {'lectures_list': lectures_list, 'audiences_list': audiences_list})


def lectures(request):
    lectures_list = Lecture.objects.order_by('audience_number')
    return render(request, 'lectures/lectures.html', {'lectures_list': lectures_list})
