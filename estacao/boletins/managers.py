from django.db import models


class BoletinQuerySet(models.QuerySet):
    def climatologico(self):
        return self.filter(category='climatologico')

    def trimestral(self):
        return self.filter(category='trimestral')

    def mensal(self):
        return self.filter(category='mensal')

    def tecnico(self):
        return self.filter(category='tecnico')
