from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter=','))
    res_data = []
    tmp = {}
    for i in range(1, len(data)):
            tmp['Name'] = data[i][1]
            tmp['Street'] = data[i][4]
            tmp['District'] = data[i][6]
            res_data.append(tmp)
            tmp = {}
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(res_data, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)


