from django.shortcuts import render


def home(request):
    from django.http import HttpResponse
    return render(request, 'home.html')
