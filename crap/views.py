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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    r = s.get('https://www.worldometers.info/coronavirus/country/us/', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    divs = soup.find_all('div', class_="maincounter-number")
    return divs[0].text, divs[1].text
