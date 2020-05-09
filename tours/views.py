from plural_ru import ru
from random import sample

from django.http import Http404
from django.shortcuts import render
from django.views import View
from plural_ru import ru

from tours.data import departures, description, subtitle, title, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
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
    def get(self, request, tour_id, *args, **kwargs):
        context = dict(tours[tour_id])
        context['departure'] = departures[context['departure']][3:]
        return render(request, 'templates/tour.html', context)


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        departure_tours = list()
        context = {'price_min': 1000000,
                   'price_max': 0,
                   'nights_min': 365,
                   'nights_max': 0,
                   'departure': departures[departure][3:]
                   }
        for i in tours:
            if tours[i]['departure'] == departure:
                tour = dict(tours[i])

                context['nights_max'] = \
                    max(context['nights_max'], tours[i]['nights'])
                context['nights_min'] = \
                    min(context['nights_min'], tours[i]['nights'])
                context['price_max'] = \
                    max(context['price_max'], tours[i]['price'])
                context['price_min'] = \
                    min(context['price_min'], tours[i]['price'])

                tour['num'] = i

                departure_tours.append(tour)
        if departure not in departures:
            raise Http404("Departure does not exist")
        q = len(departure_tours)
        if q == 0:
            raise Http404("There isn't active tours on this departure")

        context['tours'] = departure_tours
        context['tours_quantity'] = str(q) + ' ' + ru(q, ('тур',
                                                          'тура',
                                                          'туров'))
        return render(request, 'templates/departure.html', context)
