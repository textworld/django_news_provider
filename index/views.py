from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from datetime import date


# Create your views here.
def index(request):
    print(Activity.objects.filter(hold_date__gte=date.today()))
    return HttpResponse("Hello World")