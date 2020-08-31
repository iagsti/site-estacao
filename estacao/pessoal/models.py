from django.db import models


class TeamModel(models.Model):
    name = models.CharField('nome', max_length=128)
    role = models.CharField('cargo', max_length=128)
    image = models.FileField('imagem', upload_to='team/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'
