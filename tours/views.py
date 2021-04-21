from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render

from random import randint

from .data import departures, description, subtitle,  title, tours


def make_random_hotels_list():
    random_hotels_list = []
    for i in range(16):
        index = randint(1, 16)
        hotel = {index: tours[index]}
        if hotel not in random_hotels_list and len(random_hotels_list) < 6:
            random_hotels_list.append(hotel)
    return random_hotels_list


def get_departure_tours_list(departure):
    departure_tours_list = []
    for key, value in tours.items():
        if value['departure'] == departure:
            departure_tours_list.append({key: value})
    for tour in departure_tours_list:
        for key, value in tour.items():
            if {key: value} == departure_tours_list[0]:
                min_price = value['price']
                max_price = 0
                min_nights = value['nights']
                max_nights = 0
            if value['price'] < min_price:
                min_price = value['price']
            if value['price'] > max_price:
                max_price = value['price']
            if value['nights'] < min_nights:
                min_nights = value['nights']
            if value['nights'] > max_nights:
                max_nights = value['nights']
    return departure_tours_list, min_price, max_price, min_nights, max_nights


def main_view(request):
    return render(request, 'index.html', {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'hotels': make_random_hotels_list(),
        'departures': departures,
    })


def departure_view(request, departure):
    tours_list, min_price, max_price, min_nights, max_nights = get_departure_tours_list(departure)
    return render(request, 'departure.html', {
        'tours_list': tours_list,
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
        'departures': departures,
        'departure': departures[departure],
    })


def tour_view(request, id):
    tour = tours[id]
    departure = departures[tour['departure']]
    return render(request, 'tour.html', {
        'tour': tour,
        'departure': departure,
        'departures': departures,

    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Здесь ничего нет')


def custom_handler500(request):
    return HttpResponseServerError('На сервере что-то сломалось')
