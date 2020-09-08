from django.urls import path

from .views import boletins_index

app_name = 'boletins'

urlpatterns = [
    path('', boletins_index, name='index')
]
