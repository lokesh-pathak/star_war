import requests

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from app.models import StarWars


class HomeView(View):
    """
        :return all star_wars table data which is saved by user
        :render template
    """
    def get(self, request):
        res = StarWars.objects.all()
        return render(request, "app/index.html", {'data': res})


class AddData(View):
    """
        :params request data
        :redirct to root directory after save titles into database
    """
    def get(self, request):
        StarWars.objects.update_or_create(title=request.GET['name'])
        return HttpResponseRedirect('/')


def get_data(name, search_by):
    """
        :param name, search_by
        :read swapi url with page number and search element
        :return: total result
    """
    total_results = []
    for page_num in range(1, 7):
        response = requests.get('https://swapi.co/api/' + search_by, params={'search': name, 'page': str(page_num)})
        if response.status_code == 200:
            data = response.json()
            total_results = total_results + data['results']
    return total_results


class Search(View):
    def get(self, request):
        return HttpResponseRedirect('/')

    def post(self, request):
        """
            :call get_data method and pass the arguments
            :return result
            :render template
        """
        res = get_data(request.POST['name'], request.POST['search_by'])
        return render(request, "app/result.html", {'data': res})

