from django.db import models
from estacao.core.data_transform import DataTransform


class ConditionsManager(models.Manager):
    def max_temperature(self):
        return self.order_by('data').filter(tmax__isnull=False).last()

    def min_temperature(self):
        return self.order_by('data').filter(tmin__isnull=False).last()

    def relative_humidity(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        data_transform = DataTransform()
        rh = data_transform.rh(tseco=data.tseco, tumido=data.tumido, p_hpa=data.pressao)
        return round(rh, 2)

    def td(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        data_transform = DataTransform()
        td = data_transform.td(data.tseco, data.tumido, data.pressao)
        return round(td, 2)

    def p_hpa(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        data_transform = DataTransform()
        p_hpa = data_transform.pressao(data.pressao, data.temp_bar)
        return round(p_hpa)

    def visibility(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        data_transform = DataTransform()
        visibility = data_transform.visibility(data.vis)
        return visibility

    def nuvens_baixas(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        if not data.tipob:
            return '-------'
        return '%s - %d/10' % (data.tipob, data.qtdb)

    def nuvens_medias(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        if not data.tipom:
            return '-------'
        return '%s - %d/10' % (data.tipom, data.qtdm)

    def nuvens_altas(self):
        data = self.order_by('data').filter(tmax__isnull=False).last()
        if not data.tipoa:
            return '-------'
        return '%s - %d/10' % (data.tipoa, data.qtda)

    def conditions_latest(self):
        return self.order_by('data').last()