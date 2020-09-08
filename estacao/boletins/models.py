from django.db import models
from django.utils.translation import gettext as _


class Boletin(models.Model):
    CATEGORY_CHOICES = (
        ('climatologico', 'Boletim climatológico'),
        ('trimestral', 'Boletim trimestral'),
        ('mensal', 'Boletim mensal'),
        ('tecnico', 'Relatório técnico'),
    )

    title = models.CharField(_("Títlo"), max_length=50)
    category = models.CharField(
        _("Categoria"), max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(_("Arquivo"), upload_to='boletins')
