import json
import re

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from app.models import StarWars
# Create your views here.


def HomeView(request):
    res = StarWars.objects.all()
    return render(request, "app/index.html", {'data': res})


class AddData(View):

    def get(self, request):
        StarWars.objects.update_or_create(title=request.GET['name'])
        return HttpResponseRedirect('/')


class Film(View):

    def post(self, request):
        with open('films.json') as json_file:
            data = json.load(json_file)
            name = re.compile(request.POST['name'], re.IGNORECASE)
            res = list(filter(lambda x, y=name: y.search(x), data['films']))
            return render(request, "app/result.html", {'data':res})


class Planet(View):

    def post(self, request):
        with open('planets.json') as json_file:
            data = json.load(json_file)
            name = re.compile(request.POST['name'], re.IGNORECASE) 
            res = list(filter(lambda x, y=name: y.search(x), data['planets']))     
            return render(request, "app/result.html", {'data':res})

