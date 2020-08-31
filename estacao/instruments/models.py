from django.db import models
from django.utils.translation import gettext as _


class Instruments(models.Model):
    title = models.CharField(_("título"), max_length=50)
    text = models.TextField(_("texto"), max_length=2048)
    image = models.FileField(_("imagem"), upload_to='instruments')

    def __str__(self):
        return self.title
