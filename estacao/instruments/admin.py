from django.contrib import admin
from django.utils.html import format_html

from estacao.instruments.models import Instruments


class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo_image']

    def photo_image(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.image.url)


admin.site.register(Instruments, InstrumentsAdmin)
