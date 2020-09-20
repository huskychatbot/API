import json
import re

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
#
# return requests.get(url).json()
# Create your views here.

# define home function
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    # build a request object
    data = request.body.decode('utf-8')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=88b029b2c8b1fc70a1a5f2cf57de2855'
    fulfillmentText = {}
    if data != '':
        req = json.loads(request.body.decode('utf-8'))
        # get action from json
        action = req.get('queryResult').get('action')
        # get the city name
        city = req.get('queryResult').get('parameters').get('geo-city')
        if city[-1] != '市':
            city += '市'
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types
        # return a fulfillment message
        print(city)
        print(city_weather)
        fulfillmentText = {'fulfillmentText': str(city) + '的天气是' + str(city_weather.get('main').get('temp')) + '华氏度'}
        # return response
    return JsonResponse(fulfillmentText, safe=False)
