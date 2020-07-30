from django.shortcuts import render
from .models import *

import datetime, pytz

def index(request):
    list_of_model = list(map(
        lambda item: {
            'id': item.id,
            'name': item.name,
            'date': (item.date.astimezone(pytz.timezone('Europe/Moscow'))).strftime('%H:%M:%S %d-%m-%Y')

        },
        Test.objects.all()
    ))

    context = {
        'letters': list_of_model
    }

    return render(request, 'app1/index.html', context=context)
