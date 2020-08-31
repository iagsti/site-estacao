from django.shortcuts import render

from estacao.instruments.models import Instruments


def instruments_index(request):
    instruments = Instruments.objects.all()
    context = {'instruments': instruments}
    return render(request, 'instruments.html', context=context)
