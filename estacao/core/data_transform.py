import math

class DataTransform():
    def ep(self, temp):
        if temp == 0.0:
            return 0
        ep = 1.0044 * 6.112 * math.exp((17.62 * temp) / (temp + 243.12))
        return ep

    def pressao(self, pressao, temp_bar):
        p0 = pressao * (1 - 0.000163 * temp_bar)
        preshPa = (p0 - 1.3) * 1013.25 / 760
        return preshPa

    def rh(self, tseco, tumido, p_hpa):
        e = self.ep(tumido) - p_hpa * (tseco - tumido) * 0.000653 * (1 + (0.000944 * tumido))
        es = self.ep(tseco)
        rh = (e / es) * 100
        return rh

    def td(self, tseco, tumido, p_hpa):
        e = self.ep(tumido) - 0.000653 * (1 + 0.000944 * tumido) * p_hpa * (tseco - tumido)
        const_1 = e / (6.112 * 1.0044)
        const_2 = e / (6.112 * 1.004)
        td = 243.12 * (math.log(const_1)) / (17.67 - math.log(const_2))
        return td

    def windchill(self, tseco, vento):
        v = vento * 3.6
        twc = 13.12 + 0.6215 * tseco - 11.37 * math.pow(vento, 0.16) + 0.3965 * tseco * math.pow(vento, 0.16)
        return twc

    def visibility(self, index):
        range = ['menos de 50 m', '50 a 200 m', '200 a 500 m', '500 a 1000 m', '1 km a 2 km', '2 km a 4 km',
                    '4 km a 10 km', '10 km a 20 km', '20 km a 50 km', 'maior que 50 km']
        return range[index]