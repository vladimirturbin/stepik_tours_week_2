from random import sample

from django.shortcuts import render
from django.views import View

from tours.data import departures, description, subtitle, title, tours


class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        context = {
            'description': description,
            'subtitle': subtitle,
            'title': title,
            'tours': list(),
        }
        # делаем list из шести случайных туров
        for i in sample(list(tours), 6):
            tour = dict(tours[i])
            tour['num'] = i
            context['tours'].append(tour)

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
