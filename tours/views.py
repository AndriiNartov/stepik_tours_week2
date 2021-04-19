from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

# Create your views here.


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Здесь ничего нет')


def custom_handler500(request):
    return HttpResponseServerError('На сервере что-то сломалось')
