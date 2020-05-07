from django.shortcuts import render
from django.views import View

from tours.data import departures, tours


class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        context = {}
        return render(request, 'templates/index.html', context)


class TourView(View):
    @staticmethod
    def get(request, tour_id, *args, **kwargs):
        context = dict(tours[tour_id])
        # Я исправил первую заглавную И поля 'departure' на строчную потому,
        # что "Вьетнам из Екатеринбурга" выглядит эстетично,
        # А "Вьетнам Из Екатеринбурга" Выглядит Как-То Глупо.
        context['departure'] = 'и' + departures[context['departure']][1:]
        return render(request, 'templates/tour.html', context)


class DepartureView(View):
    @staticmethod
    def get(request, departure, *args, **kwargs):
        context = {}
        return render(request, 'templates/departure.html', context)
