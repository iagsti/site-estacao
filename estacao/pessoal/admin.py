from django.contrib import admin
from estacao.pessoal.models import TeamModel
from django.utils.html import format_html
from django.conf import settings


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'photo_image']

    def photo_image(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.image.url)

admin.site.register(TeamModel, TeamAdmin)
admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.SITE_INDEX_TITLE