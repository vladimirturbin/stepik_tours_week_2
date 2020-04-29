from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'templates/index.html', context)


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        context = {}
        return render(request, 'templates/tour.html', context)


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        context = {}
        return render(request, 'templates/departure.html', context)
