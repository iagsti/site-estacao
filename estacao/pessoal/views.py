from django.shortcuts import render
from estacao.pessoal.models import TeamModel


def pessoal_index(request):
    team = TeamModel.objects.all()
    
    context = {'team': team}
    return render(request, 'pessoal_index.html', context)