from django.shortcuts import render


def home(request):
    context = {'conditions': ''}
    return render(request, 'home.html', context)
