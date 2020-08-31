from django.urls import path

from .views import instruments_index

app_name = 'instruments'

urlpatterns = [
    path('', instruments_index, name='instruments_index')
]
