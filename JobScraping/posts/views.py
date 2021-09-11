from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    return render(request, 'index.html')


def internshala(request):
    jobs = models.internshala.objects.all()
    return render(request, 'internshala.html', {'jobs': jobs})


def iimjobs(request):
    jobs = models.iimjobs.objects.all()
    return render(request, 'iimjobs.html', {'jobs': jobs})


def talentracker(request):
    jobs = models.talentrack.objects.all()
    return render(request, 'talentracker.html', {'jobs': jobs})


def interesting_urls(request):
    urls = models.interesting_urls.objects.all()
    return render(request, 'interesting_urls.html', {'urls': urls})


def non_interesting_urls(request):
    urls = models.non_interesting_urls.objects.all()
    return render(request, 'non_interesting_urls.html', {'urls': urls})
