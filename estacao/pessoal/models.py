from django.db import models


class TeamModel(models.Model):
    name = models.CharField('nome', max_length=128)
    role = models.CharField('cargo', max_length=128)
    image = models.CharField('imagem', max_length=128)
