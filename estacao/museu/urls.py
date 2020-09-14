from django.urls import path
from estacao.museu.views import museu_index


app_name = 'museu'

urlpatterns = [
    path('', museu_index, name='index')
]
