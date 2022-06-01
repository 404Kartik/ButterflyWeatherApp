import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from django.urls import resolve
from .forms import CityForm

# Index function uses Openweather api to pass in the city name and return the current weather of the city
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = 'London'
    City.objects.all().delete()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)


def delete_everything(self):
    City.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))


def ip_loc(self):
    form = CityForm()
    from requests import get
    response = requests.get('https://api64.ipify.org?format=json').json()
    ip = response['ip']
    latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')
    print(latlong)
    city = get('https://ipapi.co/{}/city/'.format(ip)).text.split(',')[0]
    response = get(
        'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=271d1234d3f497eed5b1d80a07b3fcd1'.format(
            latlong[0],
            latlong[
                1])).json()
    tempKelvin = round(kelvinToCelsius(response['main']['temp']), 2)
    weather_data = []
    city_weather = {
        'city': city,
        'temperature': tempKelvin,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    weather_data.append(city_weather)
    context = {'weather_data': weather_data, 'form': form}

    return render(self, 'weather/weather.html', context)


def kelvinToCelsius(kelvin):
    return kelvin - 273.15
