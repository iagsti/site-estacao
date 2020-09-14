from django.contrib import admin

from estacao.boletins.models import Boletin


class BoletinAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'file']


admin.site.register(Boletin, BoletinAdmin)
