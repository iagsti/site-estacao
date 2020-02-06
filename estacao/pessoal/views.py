from django.shortcuts import render


def pessoal_index(request):
    team = [dict(name='Dr. Thomas Jeferson', role='Chefe da Seção Técnica de Serviços Meteorológicos',
                                image='https://i.picsum.photos/id/866/300/200.jpg')]
    
    context = {'team': team}
    return render(request, 'pessoal_index.html', context)