from django.urls import path
from estacao.contact.views import contact_index

app_name = 'contact'


urlpatterns = [
    path('', contact_index, name='contact_index')
]
