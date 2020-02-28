from django.shortcuts import render
from estacao.core.models import Dados


def home(request):
    conditions = make_conditions(Dados.objects)
    context = {'conditions': conditions}
    return render(request, 'home.html', context)


def make_conditions(conditions):
    dados = Dados.objects.max_temperature()
    ur = Dados.objects.relative_humidity()
    td = Dados.objects.td()
    p_hpa = Dados.objects.p_hpa()
    visibility = Dados.objects.visibility()
    nuvens_baixas = Dados.objects.nuvens_baixas()
    nuvens_medias = Dados.objects.nuvens_medias()
    nuvens_altas = Dados.objects.nuvens_altas()

    return {'temperatura_ar': dados.tseco, 'ur': ur, 'temperatura_orvalho': td,
            'temperatura_min': dados.tmin, 'temperatura_max': dados.tmax,
            'vento': dados.vento, 'dir': dados.dir, 'pressao': p_hpa,
            'visibilidade': visibility, 'nuvens_baixas': nuvens_baixas,
            'nuvens_medias': nuvens_medias, 'nuvens_altas': nuvens_altas,
            'diversos': 'Não disponível'}