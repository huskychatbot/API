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
def weather(request):
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


#
# @csrf_exempt
# def exchangerate(request):
#     url = 'https://api.exchangeratesapi.io/latest?base=USD'
#     exchangeRate_API = requests.get(
#         url).json()  # request the API data and convert the JSON to Python data types
#     # return a fulfillment message
#     USD_to_CNY_exchange = exchangeRate_API.get("rates").get("CNY")
#     CNY_total = 50 * USD_to_CNY_exchange
#     fulfillmentText = {'fulfillmentText': '人民币' + str(round(CNY_total)) + '元 ， 换成美元是50。'}
#     # return response
#     return JsonResponse(fulfillmentText, safe=False)


@csrf_exempt
def exchangeRate(request):
    # build a request object
    data = request.body.decode('utf-8')
    url = 'https://api.exchangeratesapi.io/latest?base=USD'
    fulfillmentText = {}
    exchangeRate_API = requests.get(
        url).json()  # request the API data and convert the JSON to Python data types
    # return a fulfillment message
    USE_to_CNY_exchange = exchangeRate_API.get("rates").get("CNY")
    CNY_total = 50 * USE_to_CNY_exchange
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    # action = req.get('queryResult').get('action')
    # req = json.loads(request.body.decode('utf-8'))
    number = req.get('queryResult').get('parameters').get('number-integer')
    # print(reqs)

    if action == '010':
        # number1 = req.get('queryResult').get('outputContexts')[0].get('number.original')
        charge = int(number) - CNY_total
        fulfillmentText = {'fulfillmentText': '找您' + str(round(charge)) + '块，谢谢。'}
    if action == '009':
        fulfillmentText = {'fulfillmentText': '人民币' + str(round(CNY_total)) + ' ， 换成美元是50。'}

    print(fulfillmentText)
    # return response
    return JsonResponse(fulfillmentText, safe=False)
