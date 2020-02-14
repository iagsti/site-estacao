from django.shortcuts import render


def home(request):
    conditions = get_conditions()
    context = {'conditions': conditions}
    return render(request, 'home.html', context)


def get_conditions():
    conditions = dict(temperatura_ar='22.7ºC', temperatura_orvalho='18.5ºC', ur='77.3%',
                        temperatura_min='17.9 °C às 14:00', temperatura_max='26.0 °C às 15:00',
                        vento='Calmo', pressao='924.8 hPa', visibilidade='4 km a 10 km',
                        nuvens_baixas='Sc/Fc - 6/10', nuvens_medias='----', nuvens_altas='----',
                        diversos='Não Disponível')

    return conditions