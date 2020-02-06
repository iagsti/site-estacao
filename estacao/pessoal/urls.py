from django.urls import path
from estacao.pessoal.views import pessoal_index

app_name = 'pessoal'


urlpatterns = [
    path('', pessoal_index, name='pessoal_index')
]
