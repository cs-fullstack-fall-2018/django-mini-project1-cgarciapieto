from django.shortcuts import render

from .models import Timeapp


def index(request):
    latest_time_list = Timeapp.objects.all()
    context = {'latest_time_list': latest_time_list}
    return render(request, 'time_app/index.html', context)