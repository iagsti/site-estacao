from django.shortcuts import render

from .models import Boletin


def boletins_index(request):
    context = {
        'climatologico': Boletin.objects.climatologico(),
        'trimestral': Boletin.objects.trimestral(),
        'mensal': Boletin.objects.mensal(),
        'tecnico': Boletin.objects.tecnico()
    }
    return render(request, 'boletins.html', context)
