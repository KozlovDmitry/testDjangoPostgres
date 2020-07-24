from django.shortcuts import render
from .models import *

def index(request):

    context = {
        'letters': Test.objects.all()
    }

    return render(request, 'app1/index.html', context=context)
