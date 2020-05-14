from django.views import generic
from bs4 import BeautifulSoup
from .models import CovidData
import requests


class IndexView(generic.ListView):
    template_name = 'crap/index.html'
    context_object_name = 'data'
    model = CovidData

    def get_queryset(self):
        cases, deaths = myfunc()
        new_data = CovidData.objects.get(id=1)
        new_data.total_infections = cases
        new_data.total_deaths = deaths
        new_data.save()
        return new_data


def myfunc():
    s = requests.Session()
    r = s.get('https://www.worldometers.info/coronavirus/country/us/')
    soup = BeautifulSoup(r.text, 'lxml')

    divs = soup.find_all('div', class_="maincounter-number")
    return divs[0].text, divs[1].text
