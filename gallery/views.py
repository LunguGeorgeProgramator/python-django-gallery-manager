from django.shortcuts import render
import random


def index(request):
    return render(request, 'index.html', {'var_test': 's'})

def view(request):
    return render(request, 'view.html', {'var_test': 's2'})