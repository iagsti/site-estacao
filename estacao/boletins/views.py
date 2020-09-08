from django.shortcuts import render


def boletins_index(request):
    context = {'boletins': {}}
    return render(request, 'boletins.html', context)
